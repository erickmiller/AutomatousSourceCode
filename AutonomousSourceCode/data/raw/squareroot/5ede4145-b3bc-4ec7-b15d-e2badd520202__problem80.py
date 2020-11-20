#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Square root digital expansion

from decimal import *

getcontext().prec = 110
squares = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
squareRootDigitSum = 0

def squareRoot(n):
	x = (Decimal(1) + n) / Decimal(2)
	old = Decimal(-1)
	while True:
		x = Decimal('0.5') * (x + n / x)
		if old == x:
			break
		else:
			old = x
	return x

def digitSum(n):
	#print(n)
	c = 0
	tmp = n
	s = 0
	while tmp != Decimal(0) and c < 100:
		digit = int(tmp)
		s += digit
		tmp -= Decimal(digit)
		tmp *= Decimal(10)
		c += 1
	return s

for i in range(1, 100):
	if i not in squares:
		ds = digitSum(squareRoot(Decimal(i)))
		squareRootDigitSum += ds

print(squareRootDigitSum)
