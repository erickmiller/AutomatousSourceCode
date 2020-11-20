# Compute the square root of a real number
# Comlpexity = O(log n)

from __future__ import division

def square_root(val):

	if 0.0 < val < 1.0:
		l = float(val)
		u = 1.0

	if val >= 1.0:
		l = 1.0
		u = float(val)

	while (l + 0.0001 < u):
		m = l + (u-l)/2.0

		if ( (m*m) - 0.01 < val < (m*m) + 0.01 ):
			return m
		if (m * m > val):
				u = m
		if (m * m < val):
				l = m
		
print "%.5f" % square_root(9.0)
print "%.5f" % square_root(8.0)
print "%.5f" % square_root(25)
print "%.5f" % square_root(0.25)
