#!/usr/bin/env python
# Comments come directly from the algorithm
# on http://en.wikipedia.org/wiki/Baby-step_giant-step

from collections import defaultdict
import math

def getPrivateKey(p, g, y):
	
	# m = Ceiling(sqrt(n))
	squareRootP = int(math.ceil(math.sqrt(p)))

	# Creating a dict as a hashmap.
	precomputedValues = defaultdict()
	

	# For all j where 0 <= j < m:
	for i in range(0, squareRootP):
		
		# Compute aj and store the pair (j, aj) in a table.
		precomputedValues[pow(g, i, p)]=i

	# Setting initial value as 0
	privateKey = 0
	
	# Compute a^-m
	minusRoot = (g**-(squareRootP))%p
	
	# y = b
	t = y
	
	# For i = 0 to (m-1)
	for i in range(0, squareRootP-1):

		# Check to see if y is the second component (aj) of any pair in the table.
		if(t in precomputedValues):
			
			#If so, return im + j
			computedKey = precomputedValues(t)
			privateKey = (i*squareRootP)+computedKey
			return privateKey

		else:
			
			# If not, y = y * a^-m (pre-computed)
			t = (t*minusRoot)%p

privateKey = getPrivateKey(85754635859,181673,34109547043)
print privateKey


