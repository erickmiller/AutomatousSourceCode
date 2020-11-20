#!/usr/bin/env python3
import sys

def squareRoot(number):
	num1 = 1
	num2 = 0.5*(1+int(number))
	while abs(num1 - num2) > 0.0001:
		num2 = num1
		num1 = 0.5*(num2 + int(number)/num2)
	return num1;
	
	
print ("The square root of " + sys.argv[1] + " is " + str(squareRoot(sys.argv[1])))