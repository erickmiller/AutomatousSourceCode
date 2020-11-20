#!/usr/local/bin/python

import sys

usage = """        Find square root of a give number

        Usage: findSquareRoot.py <number>
        Example: findSquareRoot.py 16"""

def main(argv):
    """
    Executes the main() flow
    @param argv: Command-line arguments
    @type argv: array of strings
    """
    if (len(argv) != 1):
        print usage
        sys.exit(2)
    num = float(argv[0])
    print 'Input number: ', num
    squareRoot = getSquareRoot(num)
    print 'Square root: ', squareRoot

def getSquareRoot(num):
    """
    Finds square root of a given number
    @param num: Number
    @type num: integer
    """
    isNegative = False
    if (num < 0):
        isNegative = True
        num = abs(num)

    # start with guess num / 2
    guess = num / 2

    # try to find square root within range
    while (abs(guess * guess - num) > 0.001):
        print guess
        guess = (guess + num / guess) / 2

    if (isNegative):
        return str(guess) + " i"

    return guess

if __name__ == "__main__":
    main(sys.argv[1:])