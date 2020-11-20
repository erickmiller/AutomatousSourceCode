#!/usr/bin/python

def largest_prime_factor(number):
    result = prime_factors(number)
    if result: result[-1]
    return result

def prime_factors(number):
    factors = []
    for n in xrange(2,number/2):
        if number % n == 0 and is_prime(n):
            factors.append(n)
    return factors

def is_prime(number):
    # Use the trial division with square root technique to figure out if a
    # number is prime
    if number % 2 == 0: return False

    for n in xrange(2, int(number**0.5)+1):
        if number % n == 0:
            return False
    return True

def main():
    print largest_prime_factor(600851475143)

if __name__ == "__main__": main()
