import math
def mySqrt(n):
	"""
	newton's method for finding square root

	iterative method for finding value of f(x) = 0
	s' = s - f(s)/f'(s)
	"""
	delta = 1e-10
	s = n//2
	for i in range(100):
		s = 0.5 * ( s + n / s )
		if abs( s ** 2 - n ) < delta :
			break
	return s

def testMySqrt():
	print mySqrt(4.)
	print mySqrt(2.)
	print mySqrt(10001.)

testMySqrt()