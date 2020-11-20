import sys
import math
from datetime import datetime as dt

def timedelta_to_microseconds(td): # http://stackoverflow.com/a/2416049
	return td.microseconds + (td.seconds + td.days * 86400) * 1000000.0
	
def calculate_height(x, r):
	# we could use an integer square root algorithm, e.g.
	# http://code.activestate.com/recipes/577821-integer-square-root-function/
	# that method is slower but will work for very large values of r
	return math.floor(math.sqrt(r**2 - x**2))

def circle_area(r): # numerically integrate using the rectangle rule with delta = 1
	return sum(calculate_height(x, r) for x in xrange(r))
	
def square_area(r):
	return r**2
	
def calculate_pi(r):
	return (4.0 * circle_area(r)) / square_area(r)

radius = int(sys.argv[1])
before = dt.now()
pi = calculate_pi(radius)
elapsed = dt.now() - before
print 'pi = ' + str(pi)
print 'time elapsed: ' + str(elapsed)
print 'microseconds per operation: ' + str(timedelta_to_microseconds(elapsed)/(radius))