# -*- coding: utf-8 -*-

import math

def square_root(a):
	x = a / 2.0
	while True:
	    y = (x + a/x) / 2.0
	    if abs(y-x) < 0.001:
	        break
	    x = y
	return y

print square_root(4)
print square_root(9)
print square_root(16)
print square_root(25)
print square_root(100)
print square_root(8)
print square_root(15)
