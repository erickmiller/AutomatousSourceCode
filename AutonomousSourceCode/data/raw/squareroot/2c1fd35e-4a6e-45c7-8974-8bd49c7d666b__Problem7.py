#! /usr/local/bin/python3.1

from math import sqrt

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10001st prime number?
#
# Answer:
#

def isPrime (candidate):
    """
    Determines if candidate is prime or not.
    """
    if ((candidate % 2) == 0):
        if (candidate == 2):
            return True
        else:
            return False

    squareRoot = sqrt(candidate)
    i = 3
    while (i <= squareRoot):
        if ((candidate % i) == 0):
            return False
        i += 2

    return True

def findNthPrime (n):
    """
    Find the nth prime
    """
    candidate = 3
    counter = 1
    while (counter < n):
        if isPrime(candidate):
            counter += 1
        candidate += 2

    candidate -= 2
    print(candidate)
    

def Problem7 (n):
    findNthPrime(n)

Problem7(10001)
