#!/usr/bin/env python
#
# Project Euler 80

from math import sqrt

def bigger(root, base, offset):
    root = int(root)
    return (root * root) > (int(base) * (10 ** offset))

def root(n, digits):
     base = str(n)
     root = str(int(sqrt(n)))
     offset = 0
     while len(root) < digits:
         offset += 2             
         root += "9"
         for digit in "876543210":
             if bigger(root, base, offset):
                 root = root[:-1] + digit
     return root

def digital_sum(n):
    return sum([int(x) for x in str(n)])

def square(n):
    return n in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def solution():
    return sum([digital_sum(root(x,100))
                for x in [y for y in xrange(1,101) if not square(y)]])

if __name__ == "__main__":
    print solution()
