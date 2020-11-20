from __future__ import division
from random import random

def heron_square_root(x, guess=):
	g = random() * x
	print "Trying %d" % g
	print round(g**2, 4)

	if round(g**2, 2) == round(x, 2):
		return g
	else:
		return heron_square_root((g + x/g) / 2)

heron_square_root(25)