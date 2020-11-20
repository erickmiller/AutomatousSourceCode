#Thinkpython chapter 7 exercise 7.3

#Test my sqrt estimating function against math.sqrt

import math


def square_root(n):
	"""
		epsilon_constant is used to determine how close the approximation needs to be
		x is initial estimate. y is the output of the formula, which is used as the 
		estimate for the next pass. loop runs until successive estimates
		are very close.

	"""
	epsilon_constant = .0000000000000001
	x = n
	y = n
	while True:
		x = y
		y = (float(x) + (float(n)/float(x)))/2
		if abs(y-x) < epsilon_constant:
			break
	return y


def test_square_root(n):
	for i in range(n):
		print str(i+1).rjust(4), 
		print str(square_root(i+1)).rjust(15),
		print str(math.sqrt(i+1)).rjust(15),
		print str(abs(square_root(i+1) - math.sqrt(i+1))).rjust(15)


test_square_root(10)