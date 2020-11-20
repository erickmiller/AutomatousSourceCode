from math import sqrt

def squareRootBi(x, epsilon):
	"""Assumes < >= 0 and epsilon > 0
	return y s.t. y * y is with in epsilon of x"""
	assert x >= 0, + str(x)
	assert epsilon > 0, + str(epsilon)
	low = 0
	high = x
	guess = (low + high) / 2.0
	ctr = 1  # counter
	while abs(guess **2 - x) > epsilon and ctr <= 100:
		if guess ** 2 < x:
			low = guess
		else:
			high = guess
		guess = (low + high)/2.0
		ctr += 1
	assert ctr <= 100
	print 'Bi method. NumIterations:', ctr, ' Estimate:', guess
	return guess

print squareRootBi(20000000000000000000, 0.01)
print sqrt(200000000000000000000)