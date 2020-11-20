# -*- coding: utf-8 -*-
# Problem 80
# Square root digital expansion

# It is well known that if the square root of a natural number is not an integer,
# then it is irrational. The decimal expansion of such square roots is infinite
# without any repeating pattern at all.

# The square root of two is 1.41421356237309504880..., and the digital sum of the
# first one hundred decimal digits is 475.

# For the first one hundred natural numbers, find the total of the digital sums
# of the first one hundred decimal digits for all the irrational square roots.

from time import time
import decimal


def digit_sums(n):
    """
    take the square root of "n", get rid of ".", kep the first 100 digits,
    then return the sum of the 100 digits
    """
    decimal.getcontext().prec = 105     # seems that 100 is not precise enough

    square_root_str = str(decimal.Decimal(n).sqrt()).replace(".", "")[:100]
    return sum(map(int, square_root_str))
    
start_time = time()

perfect_squares = [i ** 2 for i in xrange(1, 11)]

sum_ = 0
for i in xrange(1, 101):
    if not i in perfect_squares:
        sum_ += digit_sums(i)

print "Answer:", sum_

print "Total Time: ", time() - start_time

# Completed on Sat, 29 Mar 2014, 23:16
# Solve by:  10044
# ---------------
# Answer: 40886
# Total Time:  0.0119998455048
# [Finished in 0.2s]
