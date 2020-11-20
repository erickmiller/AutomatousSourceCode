__author__ = 'Brennan'

from euler5 import is_evenly_divisible
import itertools
import math


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True

    # we only need to check up to the sqrt of n.
    square_root = int(math.ceil(math.sqrt(number)))
    top_of_range = square_root + 1
    # we don't need to check any even numbers besides 2.
    range_to_check = itertools.chain([2], range(3, top_of_range, 2))

    for divisor in range_to_check:
        if is_evenly_divisible(divisor, number):
            return False
    return True


def get_nth_prime(n):
    prime_count = 0
    for x in itertools.count(1):
        if is_prime(x):
            prime_count += 1
            print("prime " + str(prime_count) + ": " + str(x))
        if prime_count == n:
            return x


            # print(get_nth_prime(10001))