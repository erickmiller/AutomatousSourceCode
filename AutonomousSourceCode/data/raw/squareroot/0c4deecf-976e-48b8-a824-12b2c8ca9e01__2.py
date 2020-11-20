def square_root(a, x):
	y = ( x + a/x) / 2
	if y == x:
		return y
	return square_root(a, y)


print square_root(4,3)
