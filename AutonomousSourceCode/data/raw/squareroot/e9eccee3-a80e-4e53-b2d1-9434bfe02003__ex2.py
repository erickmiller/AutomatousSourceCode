


def square_root(a, iters=4):
		"""a = number to find the square root of 
		x = number of passes
		square_root calculates a square root using Newton's method
		"""
		y = 0
		x = a/3
		for i in range(iters):
				y = (x + a/x) / 2
				x = y
				#print (" guess is {0}".format(y))
		
		return y

print(square_root(4))
print(square_root(3))
print(square_root(4,20))
print(square_root(3,20))
		
