def square_root(n):
	n=float(n)
	x=n/2
	i=0
	while i<10:
		x=((x+n)/x)/2
		i=i+1
	return x

print square_root(9)
