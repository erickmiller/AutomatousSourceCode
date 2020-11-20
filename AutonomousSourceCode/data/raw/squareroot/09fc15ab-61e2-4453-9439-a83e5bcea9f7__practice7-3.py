# -*- coding: utf-8 -*-

import math

# math.sqrt fuction

def square_root(a):
	x = a
	while True:
	    y = (x + a/x) / 2.0
	    if abs(y-x) < 0.001:
	        break
	    x = y
	return y

def test_square_root(a):
	ary = []
	ary.append(a)
	ary.append(square_root(a))
	ary.append(math.sqrt(a))
	ary.append(abs(ary[1]-ary[2]))
	return ary

i = 1
while i < 10:
	print test_square_root(i)
	i = i + 1