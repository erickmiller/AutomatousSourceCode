import math

def newt_meth_while(s):
	"""
	Determines square root of value using Newton's
	method, using while loop.

	Values of 4 or greater are checked against an
	estimate of half their value.

	Values less than 4 are computed using built-in
	square root function from math module.
	"""
	if s >= 4:
		e = s / 2
	else:
		print math.sqrt(s)
		return
	while True:
		print e
		y = (e + s/e) / 2
		if y == e:
			break
		e = y

def newt_meth_recurse(s):
	"""
	Determines square root of value using Newton's
	method, using recursion.

	Values of 4 or greater are checked against an
	estimate of half their value.

	Values less than 4 are computed using built-in
	square root function from math module.
	"""
	if s >= 4:
		e = s / 2
	else:
		print math.sqrt(s)
		return
	y = (e + s/e) / 2
	print y
	if e != y:
		e = y
		newt_meth(s, e)
	else:
		return
