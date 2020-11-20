def square_root(x):
	"""
	this is the ancient way to calculate the square_root
	step 1: you guess a number g, and get the result of g**2
	step 2: if it's not close enough to X, take a new guess "g" with the formula below
	step 3: go back to step 2 until it's close enough.
	"""
	g = 42.0
	while g * g - x < -0.001 or g * g - x > 0.001:
		g = (g + x / g) / 2
	return g

def test():
	print square_root(9)
	print square_root(100)
	print square_root(0)
	print square_root(25)

test()
