import sys
import os
import math

# bruce = 5
# print bruce,
# bruce = 7
# print bruce
# the output of this program is 5 7
# the comma suppresses the new line in the print statement

# Note = is an assignment, == is statement of equality

# Initialize a variable like so: x = 0; x = x + 1

# Repeating identical or similar tasks without making errors
# is something computers do well and people do poorly.

def countdown (n):
	while n > 0:
		print n
		n = n - 1
	print 'Blastoff!'

def take_break():
	while True:
		line = raw_input('> ')
		if line == 'done':
			break
		print line
	print 'Done!'

def square_root (a):
	epsilon = 0.00001
	x = a
	while True:
		y = (x + a/x) / 2
		if abs(y-x) < epsilon:
			break
		x = y
	return x

print square_root (5.00)

# Ex 7.3 
def test_square_root(a):
	print a,
	print "\t",
	x = square_root(a)
	print x,
	print "\t",
	y = math.sqrt(a)
	print y,
	print "\t",
	return abs(x-y)

print test_square_root(5)
print test_square_root(4)

def eval_loop():
	while True:
		line = raw_input('> ')
		if line == 'done':
			break
		print eval(line)
	return 'Done!'
	
# Ex. 7.5
def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial (n - 1)
		result = n * recurse
		return result

def estimate_pi():
	k = 0
	total = 0
	while True:
		den = (factorial (k)**4)*(396**(4*k))
		num = (factorial (4 * k))*(1103+26390*k)
		so = num / den
		total += so
		if so < 1e-15:
			break
		k += 1
	total = (2 * math.sqrt(2) * total) /9801
	return 1 / total

print estimate_pi()
print math.pi