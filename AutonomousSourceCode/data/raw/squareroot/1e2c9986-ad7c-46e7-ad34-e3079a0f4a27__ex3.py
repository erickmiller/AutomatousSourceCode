
from math import sqrt 

def square_root(a, iters=8):
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

for i in range(1,10):
		print("{0} {1:.9f} {2:.9f} {3}".format(i, square_root(i), sqrt(i),  abs(square_root(i) - sqrt(i))) )
		
