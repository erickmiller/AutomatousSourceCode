'''
Functions to estimate square root values.

Created on Dec 16, 2014
@author: sql.sith
'''
from __builtin__ import False, True

_tolerance = 0.001

def square_root(target):
    guess = 0
    guesses = 0

    while (abs(guess * guess - target) > _tolerance and
           guess * guess < target):
        guess += 0.00001
        guesses += 1

    if abs(guess * guess - target) > _tolerance:
        raise(_NO_GOOD_SOLUTION_FOUND)

    if _debug: print(guesses)  # @IgnorePep8

    return(guess)

global _debug
_debug = False

global _NO_GOOD_SOLUTION_FOUND
_NO_GOOD_SOLUTION_FOUND = Exception(
    "Solution found is outside specified tolerance.")

if __name__ == '__main__':
    _debug = True

    square = 65535
    sqrt = square_root(square)

    print("The square root of {0} is {1}.".format(square, sqrt))
    print(sqrt * sqrt)
