# This files contains all the operations that are used frequently (by me) while solving the problems from project euler as functions.
import math

def is_prime(num):
	"""Determines whether a number is prime or not."""
	square_root = int(math.ceil(math.sqrt(num)))
	for n in range(2, square_root+1):
		if num % n == 0:
			if num != n:
				return False

	return True

def factors(num):
	"""Finds all the factors of a given number and returns them as a list."""
	if is_prime(num) == True:
		factors = [1, num]
		return factors
	else:
		factors = [1]
		square_root = int(math.ceil(math.sqrt(num)))
		
		for n in range(2, square_root+1):
			if num % n == 0:
				factors.append(n)

		for n in range(1, len(factors)):
			new_n = num / factors[n]
			if new_n not in factors:
				factors.append(num / factors[n])

		factors.append(num)
		return factors

def prime_factors(num):
	num_factors = factors(num)
	prime_factors = []

	for n in num_factors:
		if is_prime(n):
			prime_factors.append(n)

	return prime_factors