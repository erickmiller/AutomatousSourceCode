#!/usr/bin/python3

"""
Square root digital expansion
Problem 80

https://projecteuler.net/problem=80
"""

from decimal import getcontext, Decimal

getcontext().prec = 102

def digital_sum(n):
    return sum([int(i) for i in str(n).split('.')[-1]])

# set of all numbers < 100 with an irrational square root
non_squares = set(range(100)).difference([i*i for i in range(10)])

s = 0
for i in non_squares:
    n = Decimal(str(Decimal(i).sqrt()).split('.')[-1][:-2])
    s += digital_sum(n) + int(str(Decimal(i).sqrt()).split('.')[0])

print(s)
