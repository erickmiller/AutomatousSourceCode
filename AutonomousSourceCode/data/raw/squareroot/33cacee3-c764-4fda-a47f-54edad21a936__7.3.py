from math import *


def square_root(a):
    """ calculates the square root of a number using Newton's algorithm

    a: a number
    """

    x = a / 4.0    # Providing an adequate estimate of x
    while True:
        y = (x + a/x) / 2.0
        if abs(y-x) < 0.0000001:
            break
        x = y
    return x


def test_square_root(a):
    """ Prints a table comparing the results of square_root and sqrt on a
    number a. It also provides the absolute difference between the two
    estimates
    """

    for i in range(9):
        print a, "\t",
        print square_root(a), "\t",
        print sqrt(a), "\t",
        print abs(square_root(a) - sqrt(a))
        a = a + 1


test_square_root(1.0)
