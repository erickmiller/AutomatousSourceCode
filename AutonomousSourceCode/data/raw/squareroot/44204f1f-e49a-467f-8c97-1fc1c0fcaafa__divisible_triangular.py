"""divisible_triangular.py: Problem 12 of project euler.
Finds the first triangular number to have > 500 divisors. """

import math

def count_divisors(number):
    """ Determines the number of divisors that the number
        specified has."""

    divisor_count = 0
    square_root = math.sqrt(number)

    counter = 1
    while counter <= square_root:
        if number % counter == 0:
            divisor_count += 2
        counter += 1

    if square_root * square_root is number:
        divisor_count -= 1

    return divisor_count

if __name__ == "__main__":
    CURRENT_NUMBER = 0
    COUNT = 1

    while count_divisors(CURRENT_NUMBER) < 500:
        CURRENT_NUMBER += COUNT
        COUNT += 1

    print "The first triangular number with over 500 divisors is " \
            "{0}".format(CURRENT_NUMBER)

