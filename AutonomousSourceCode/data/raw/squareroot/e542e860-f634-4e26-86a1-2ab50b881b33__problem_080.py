#!/usr/bin/env python


"""
Problem Definition :

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

"""

__author__ = 'vivek'

import time
from decimal import *


def find_sum(num):
    add = 0

    while num > 0:
        num, digit = divmod(num,10)
        add += digit

    return add


def main():

    start_time = time.clock()
    getcontext().prec = 102

    answer = 0

    for number in xrange(1, 100):
        square_root = str(Decimal(number).sqrt())

        if len(square_root) > 1:
            decimal = int(square_root[:1] + square_root[-101:-2])
            answer += find_sum(decimal)

    print(answer)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))

if __name__ == '__main__':
    main()

