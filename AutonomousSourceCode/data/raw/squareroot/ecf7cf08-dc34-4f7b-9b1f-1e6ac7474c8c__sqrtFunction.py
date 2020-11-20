def sqr(a):
	#newton method
	#http://stackoverflow.com/questions/18838265/python-square-root-function
	x = a
	for i in range(a):
		x = x-(x*x - a)/(2.0*x)
	return "{0:.2f}".format(x)
print sqr(4)