#https://github.com/AaronJiang/ProjectEuler/tree/master/py
"""
It is well known that if the square root of a natural number 
is not an integer, then it is irrational. The decimal expansion 
of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital 
sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital 
sums of the first one hundred decimal digits for all the irrational square roots.
"""
from Helper import isSquare
from math import sqrt
from decimal import getcontext, Decimal

def sumStringNumbers(n):
	total = 0
	for number in n:
		total += int(number)
	return total

def main():
	total = 0
	getcontext().prec = 102
	for n in range(2, 101):
		if not isSquare(n):
			root = str(Decimal(n).sqrt())
			root = root.replace('.','')
			total += sumStringNumbers(root[:100])
	print total

if __name__ == "__main__":
    main()
