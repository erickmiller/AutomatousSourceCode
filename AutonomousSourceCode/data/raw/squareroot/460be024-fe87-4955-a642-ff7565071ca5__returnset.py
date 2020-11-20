from math import sqrt

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b


def divide(a, b):
	print "DIVING %d / %d" % (a, b)
	return a / b

def square_root(a, b):
	
	return sqrt(a)   

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide (100, 2)


print "Age: %d, Height: %d, Weight: %d, IQ: %d. " % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

c = int(raw_input())
print "The square root of %d is %d." % (c, square_root(c, 2))




def distance(p, q):
	# Assume that v1 and v2 have the same number of elements
	dimension = len(v1)
	total = 0

	for i in range(0, dimension):
		total += (p[i] - q[i]) * (p[i] - q[i])

	return sqrt(total)

p = [0,1,5]
q = [7,8,3]
print "The Euclidean distance between v1 and v2 is: ", sqrt(sum( ((p[i] - q[i]) * (p[i] - q[i])) for i in range(0, len(p)) ))




