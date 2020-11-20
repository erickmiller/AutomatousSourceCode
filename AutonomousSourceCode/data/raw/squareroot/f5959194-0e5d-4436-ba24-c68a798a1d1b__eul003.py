#! /usr/bin/python
from __future__ import print_function
from math import sqrt

def is_prime(n):
    """returns True if n is a prime #
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    square_root = int(sqrt(n))
    if [i for i in range(2, square_root + 1) if n % i == 0]:
        return False
    else:
        return True


def largest_prime(n):
    """Returns None if n is already a prime"""
    div = 2
    while div < n:
        if n % div == 0:
            current = n / div
            if is_prime(current) and n % current == 0:
                return current
        div += 1


if __name__ == '__main__':
    x = 600851475143
    print(largest_prime(x))
