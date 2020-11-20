#!usr/bin/env python
#python3_only


import sys
import math
import pprint


def main():
	try:
		print(sqrt(9))
		print(sqrt(2))
		print(sqrt(10))
		print(is_prime(5))
		print("This never printed.")
		prime_square_divisors = {x*x:(1, x, x*x) for x in range(101)
						 if is_prime(x)}
		pp = pprint.pprint
		pp(prime_square_divisors)
	except ValueError as e:
#		print(e, file=sys.stderr)
		print("Program execution continues normally here.")


def sqrt(x):
	
	if x < 0:
		raise ValueError("Cannot compute square root"
						 " of negative number {}".format(x))
	guess = x
	i = 0
	while guess * guess != x and i < 20:
		guess = (guess + x / guess) / 2.0
		i += 1 
	return guess


def is_prime(x):
	if x < 2:
		return False
	for i in range(2, int(sqrt(x)) + 1):
		if x % i == 0:
			return False
	return True
	
	
if __name__ == '__main__':
	main()
#	[x for x in range(101) if is_prime(x)]

