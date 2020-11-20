from math import *

def print_n(s,n):
	while n > 0:
		print s
		n = n -1

def square_root(a):
	float(a)
	x = a / 2.0
	epsilon = 0.0000000001
	while True:
		y = (x+a/x)/2
		if abs(y-x) < epsilon:
			break
		else: x = y
	return y

def test_square_root(a=10):
	n = []
	for i in range(a):
		m = []
		m.append(float(i+1)) # the square number i
		m.append(square_root(m[0])) #the output o square_root(i)
		m.append(sqrt(m[0])) #the output of sqrt(i)
		m.append(abs(m[2]-m[1])) #the absolute difference of the results
		n.append(m) #list of all tests.

	#print the table

	for i in range(a):
		for j in range(4):
			d = 13 - len(str(n[i][j]))
			print n[i][j],' ' * d,
		print '\n'

def eval_loop():
	'''This needs some kind of exception handling. For the moment it only works with python-legal expressions, crashes otherwise.'''
	b = "Did nothing."
	while True:
		a = raw_input('> ')
		if a == 'done':
			print b
			break
		b = eval(a)
		print b

def estimate_pi():
	'''Function to estimate pi with Ramanujan's series, accurate to 13 decimal places.'''
	k = 0.0
	a = 0.0
	b = 0.0
	while True:
		b = (factorial(4.0*k)*(1103.0+ 26390.0*k))/(factorial(k)**4.0 * 396.0**(4.0*k))
		a += b
		if b < 1e-15: #set the accuracy
			c = ((2.0*(sqrt(2.0)))/9801.0)*a
			pi = 1.0/c
			return pi
		k += 1

