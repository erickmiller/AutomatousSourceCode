import math

def square_root(a):
	x = a/2.0
	epsilon = 0.0000000001
	while True:
		y = (x + a/x) / 2
		if abs(y-x) < epsilon:
			break
		x = y
	return x

def test_square_root(a):
	i = 1.0	
	while i <= a:
		print i,
		print square_root(i),
		print math.sqrt(i),
		print abs(square_root(i) - math.sqrt(i))
		i = i + 1

test_square_root(9)


