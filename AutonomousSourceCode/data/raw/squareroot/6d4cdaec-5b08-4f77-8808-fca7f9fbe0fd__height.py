import numpy
from PIL import Image
from random import randrange

class World:
	def __init__(self, the_size):
		global size
		global points
		size = (2**the_size)+1
		points = []
		points = self.createPoints()

	def diamondSquareAlgorithm(self, root_square):
		count = 0
		root_square.modCenter()
		c_squares = root_square.getSquareChildren()
		c_diamonds = root_square.getDiamondChildren()

		while(True):
			#Mod children diamonds
			for di in c_diamonds:
				di.modCenter()

			#Mod children squares
			for sq in c_squares:
				if(sq.tooSmall()):
					return
				sq.modCenter()

			#Get new children
			temp_squares = []
			temp_diamonds = []
			for sq in c_squares:
				temp_diamonds.extend(sq.getDiamondChildren())
				temp_squares.extend(sq.getSquareChildren())

			c_diamonds = temp_diamonds
			c_squares = temp_squares
			
			count = count + 1

	def printPoints(self):
		count = 0
		for p in points:
			print(p.h),
			count+=1
			if(count == size):
				print("")
				count = 0

	def normalizePoints(self, shades):
		shades = shades-1
		section = 255/shades
		bot = 0
		top = section
		
		while(top < 255):
			for point in points:
				if(point.h > bot and point.h <= top):
					point.h = top

			bot = top
			top = top + section

	def writePoints(self, name):
		f = open(str(name)+".txt", "w+")
		count = 0
		for p in points:
			f.write(str(p.h)+"\t")
			count+=1
			if(count == size):
				f.write("\n")
				count = 0

	def writeImage(self, name):
		im = Image.new("RGB", (size,size))
		for y in range(im.size[1]):
			for x in range(im.size[0]):
				point = self.getPoint(x,y)
				amt = point.h
				if(amt < 100):
					im.putpixel((x,y), (0,0,amt+200))
				else:
					im.putpixel((x,y), (0,amt-60,0))

		im.save(str(name)+".png")

	def createPoints(self):
		points = []

		for y in range(size):
			for x in range(size):
				points_x = []
				points_x.append(Point(x, y, 150))
				points.extend(points_x)

		return points

	@staticmethod
	def getPoint(x, y):
		if(x < 0 or x >= size or y < 0 or y >= size):
			return Point(x,y,0)

		point = points[(size * y) + x]
		return point

	@staticmethod
	def getMidpoint(point1, point2):
		return World.getPoint((point2.x+point1.x)/2, (point2.y+point1.y)/2)

	def getSize(self):
		return size


class Point:
	def __init__(self, x, y, h=0.0):
		self.x = x
		self.y = y
		self.h = h

	def setHeight(self, new_h):
		self.h = new_h

	def __str__(self):
		return str(self.x)+","+str(self.y)

class Quad:
	def __init__(self, p1, p2, p3, p4):
		self.mod = 4
		self.tl = p1
		self.tr = p2
		self.bl = p3
		self.br = p4

		self.top = p1
		self.bot = p2
		self.lef = p3
		self.rig = p4

	def getAverageHeight(self):
		return (self.tl.h+self.tr.h+self.bl.h+self.br.h)/4

	def getCenter(self):
		return World.getMidpoint(self.tl,self.br)

	def getSize(self):
		size_x = self.br.x-self.tl.x
		size_y = self.br.y-self.tl.y
		return size_x*size_y

	def modCenter(self):
		center = self.getCenter()
		avg = self.getAverageHeight()
		center.setHeight(avg+randrange(-avg/self.mod,avg/self.mod,1))
		self.mod = self.mod*2

	def tooSmall(self):
		return self.getSize()<=1

class Square (Quad):
	def getDiamondChildren(self):
		center = self.getCenter()

		top_d = Diamond(World.getPoint(center.x, self.tl.y+(self.tl.y-center.y)), center, self.tl, self.tr)
		bot_d = Diamond(center, World.getPoint(center.x, self.bl.y+(self.bl.y-center.y)), self.bl, self.br)
		left_d = Diamond(self.tl, self.bl, World.getPoint(self.tl.x+(self.tl.x-center.x), center.y), center)
		right_d = Diamond(self.tr, self.br, center, World.getPoint(self.tr.x+(self.tr.x-center.x), center.y))

		return [top_d, bot_d, left_d, right_d]

	def getSquareChildren(self):
		top = World.getMidpoint(self.tl,self.tr)
		bot = World.getMidpoint(self.bl,self.br)
		left = World.getMidpoint(self.tl,self.bl)
		right = World.getMidpoint(self.tr,self.br)
		center = World.getMidpoint(self.tl, self.br)
		
		square_tl = Square(self.tl, top, left, center)
		square_tr = Square(top, self.tr, center, right)
		square_bl = Square(left, center, self.bl, bot)
		square_br = Square(center, right, bot, self.br)

		return [square_tl, square_tr, square_bl, square_br]

	def __str__(self):
		return "TopLeft: \n"+str(self.tl)+"\nTopRight: \n"+str(self.tr)+"\nBotLeft: \n"+str(self.bl)+"\nBotRight:\n "+str(self.br)

class Diamond (Quad):
	def getCenter(self):
		return World.getMidpoint(self.top, self.bot)

	def getSquare(self):
		tl = Worldn.getMidpoint(self.top, self.lef)
		tr = World.getMidpoint(self.top, self.rig)
		bl = World.getMidpoint(self.bot, self.lef)
		br = World.getMidpoint(self.bot, self.rig)

		return Square(tl, tr, bl, br)

	def __str__(self):
		return "Top: \n"+str(self.top)+"\nBot: \n"+str(self.bot)+"\nLeft: \n"+str(self.lef)+"\nRight: \n"+str(self.rig)

class Main:
	def __init__(self):
		seed = 150
		count = 1
		world = World(9)
		size = world.getSize()-1

		tl = world.getPoint(0,0)
		tr = world.getPoint(size,0)
		bl = world.getPoint(0,size)
		br = world.getPoint(size,size)

		tl.setHeight(seed)
		tr.setHeight(seed)
		bl.setHeight(seed)
		br.setHeight(seed)

		root_square = Square(tl, tr, bl, br)

		#Recursion
		world.diamondSquareAlgorithm(root_square)

		#Normalization
		world.normalizePoints(6)

		#Print Points
		#world.printPoints()

		#Write Image
		world.writeImage("img")

main = Main()