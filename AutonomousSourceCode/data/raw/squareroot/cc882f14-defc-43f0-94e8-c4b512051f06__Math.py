#!/usr/bin/env python

"""Mathematical utilities"""

import math


#------------------------------------------------------------------------------
def isPrime(num):
    """Check if num is prime"""
    for idx in range(2, int(math.sqrt(num))):
        if not num % idx:
            return False
    return True


#------------------------------------------------------------------------------
def binomialCoeff(elements, combinations):
    """
    Calculate binomial coefficient for the given number of
    elements and combinations
    """
    fact = math.factorial
    return fact(elements) / fact(combinations) * fact(elements - combinations)


#------------------------------------------------------------------------------
def average(seq):
    """Calculate the average value of a sequence of values"""
    return sum(seq) / len(seq)


#------------------------------------------------------------------------------
def sqrt(num) -> float:
    """Calculate the square root of the given number"""
    # root = num / 2  # make a guess TODO improve first guess
    root = num / 2 if num > 0 else 1
    while abs((num / root) - root) > 0.000000001:
        root = average((root, num / root))
    return root

#------------------------------------------------------------------------------
# test
if __name__ == '__main__':
    print(0.1*0.1)
    print(sqrt(0.001))
