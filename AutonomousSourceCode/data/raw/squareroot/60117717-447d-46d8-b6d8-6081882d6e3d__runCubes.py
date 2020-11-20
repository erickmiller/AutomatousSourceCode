#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
import colorsys
import cubes
import random
import time
import math

# Size of window
SIZE = 512
# Size of squares
SCALE = 16

# Derived info about window and grid
GSIZE = int(SIZE/SCALE)-1
GCENTER = int(GSIZE/2)
X_SCALE = SCALE
Y_SCALE = SCALE

DRAW = 1
# Display grid points
GRID = 1
# Width of grid points
DASHWIDTH = 2

CW = 1
CCW = -1
X = 0
Y = 1
# Make this a dictionary
N 	= 0
NE 	= 1
E 	= 2
SE 	= 3
S 	= 4
SW 	= 5
W 	= 6
NW 	= 7

# Lists of directions for iteration
DA = [N,E,S,W]
DB = [N,NE,E,SE,S,SW,W,NW]
DC = [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1)]

OUTLINE = "#000000"
FILL = "#0047AB"

drawings = {}
squares = []

def inGroup(p):
	n = 0
	group = {p.connections[x] for x in p.connections}
	while len(group) > n:
		n = len(group)
		for s in cubes.squaresList:
			if s in group:
				for d in DA:
					if d in s.connections:
						group.add(s.connections[d])


	if len(group) == len(cubes.squaresList):
		return 1
	else:
		return 0


def adjTo(coord):
	a = 0
	for d in DA:
		if coord + d in cubes.squaresCoords:
			a = a+1
	return a

def pivotTo(dest):
	for n in range(10):
		s = random.choice(squares)
		while s.adjNum > 2:
			s = random.choice(squares)

		c1 = s.coord

		d = random.choice([CW, CCW])

		p = s.getPivot(d)

		if p:
			c2 = p[0]
			if adjTo(c2) > 1 and (abs(c2[X]-dest[X]) + abs(c2[Y]-dest[Y]) <= abs(c1[Y]-dest[Y]) + abs(c1[X]-dest[X])) :
				s.pivot(p = p)
				if inGroup(s):
					moveDrawing(s, c1, c2)
					root.update()
				else:
					s.move(c1)
				return


# Pivot a random square in a random location
def randPivot():
	while True:
		s = random.choice(squares)
		while s.adjNum > 2:
			s = random.choice(squares)
		c1 = s.coord

		d = random.choice([CW, CCW])
		if s.pivot(d):			
			c2 = s.coord
			if inGroup(s):
				moveDrawing(s, c1, c2)
				root.update()
			else:
				s.move(c1)
			return
								

# Create a new square in a random location
# 	Favors spread and long paths
def randNewSquare(event = None):
	opens = []
	picks = {0:[], 1:[], 2:[], 3:[]}
	shuffled = list(squares)
	random.shuffle(shuffled)
	for n in (0,1,2,3):
		[picks[n].append(q) for q in shuffled if q.adjNum == n]
	while(len(squares) < GSIZE*GSIZE):
		for n in (0,1,2,3):
			if picks[n]:
				for s in picks[n]:
					opens = []
					for d in DA:
						if d not in s.connections:
							opens.append(d)
					random.shuffle(opens)
					for d in opens:
						m = cubes.Square(s, d)
						if m:
							return m

# Create a new square in a random location
def randNewSquareFast():
	shuffledSquares = list(squares)
	random.shuffle(shuffledSquares)
	for s in shuffledSquares:
		if s:
			if s.adjNum < 4:
				parent = s
				break

	shuffledDirs = list(DA)
	random.shuffle(shuffledDirs)
	
	for d in shuffledDirs:
		if d not in parent.connections.keys():
			parentDir = d
			break

	return cubes.Square(parent, parentDir)

def drawSquare(square):
	x1 = ((square.coord[X]+GCENTER+1)*SCALE)
	y1 = ((-square.coord[Y]+GCENTER+1)*SCALE)
	x2 = ((square.coord[X]+GCENTER+1)*SCALE)+SCALE
	y2 = ((-square.coord[Y]+GCENTER+1)*SCALE)+SCALE
	drawing = (canvas.create_rectangle(x1, y1, x2, y2,  fill = FILL, outline = OUTLINE, width=2))
	canvas.tag_bind(drawing, '<Button-3>', lambda event, arg=square: rClick(event, arg))
	canvas.tag_bind(drawing, '<Button-1>', lambda event, arg=square: lClick(event, arg))
	drawings[square] = drawing
	root.update()




def mClick(event):
	new = randNewSquareFast()
	squares.append(new)
	drawSquare(new)
	for s in new.connections.values():
		drawSquare(s)

def lClick(event, square):
	c1 = square.coord
	square.pivot(CCW)
	c2 = square.coord
	if inGroup(square):
		moveDrawing(square, c1, c2)
		root.update()
	else:
		print("a")
		square.move(c1)
		print("b")

	# moveDrawing(square, c1, c2)

def rClick(event, square):
	c1 = square.coord
	square.pivot(CW)
	c2 = square.coord
	if inGroup(square):
		moveDrawing(square, c1, c2)
		root.update()
	else:
		print("a")

		square.move(c1)
		print("b")

	# moveDrawing(square, c1, c2)


def moveDrawing(square, c1, c2):
	x1 = c1[X]
	y1 = -c1[Y]
	x2 = c2[X]
	y2 = -c2[Y]
	dx = (x2-x1)*SCALE
	dy = (y2-y1)*SCALE
	
	canvas.move(drawings[square], dx, dy)
	root.update()


# Initialize tkinter ------------------------------------------

if DRAW:
	root = Tk()
	root.minsize(SIZE, SIZE)
	root.geometry(str(int(SIZE+SCALE)) + 'x' + str(int(SIZE+SCALE)))

	canvas = Canvas(root, width=SIZE+SCALE, height=SIZE+SCALE)
	canvas.place(relx=.5, rely=.5, anchor=CENTER)
	canvas.bind('<Button-2>', mClick)

	# Draw Grid ---------------------------------------------------

	if(GRID):
		i=SCALE
		while(i <= SIZE):
			canvas.create_line(i, SCALE, i, SIZE+DASHWIDTH, dash=(DASHWIDTH, SCALE-DASHWIDTH), width=DASHWIDTH)
			i += SCALE

# -------------------------------------------------------------


m = cubes.Square(master = 1)
squares.append(m)

while len(squares) < 50:
	new = randNewSquareFast()
	squares.append(new)


if DRAW:	
	for s in squares:
		drawSquare(s)

def rp():
	randPivot()
	# for n in range(10):
	# 	pivotTo((10,10))
	root.after(0, rp)


try:
	# root.after(0, rp)
	root.mainloop()
except:
	pass

