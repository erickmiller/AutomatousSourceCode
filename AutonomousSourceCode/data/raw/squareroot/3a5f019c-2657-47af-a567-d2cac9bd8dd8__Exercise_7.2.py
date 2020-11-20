def square_root(a):
	x = a/2.0
	epsilon = 0.0000001
	while True:
		y = (x + a/x) / 2
		if abs(y-x) < epsilon:
			break
		x = y
	return x

