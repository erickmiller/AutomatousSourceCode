import math
def square_root (a):
	guess = 1
	while abs (guess * guess - a) >= 1e-12:
		guess  = (a/ guess + guess) *0.5
	return guess

def test_square_root():
	a = 1.0
	while (a < 10):
		print (a, square_root (a), math.sqrt(a), abs (square_root (a) - math.sqrt(a)))
		a += 1

test_square_root()