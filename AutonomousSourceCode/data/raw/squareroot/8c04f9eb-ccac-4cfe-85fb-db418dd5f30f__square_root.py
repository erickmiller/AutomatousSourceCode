#!/usr/bin/env python

import sys
def square_root(num,guess):
    print 'Current guess: %f' % guess
    return 0.5*(guess + (num/guess))

def main(num,tolerance):
    first_guess = num/2.0
    approx_root = square_root(num,first_guess)
    while True:
        new_guess = square_root(num,approx_root)
        if abs(new_guess-approx_root) < tolerance:
            return new_guess
        else:
            approx_root = new_guess

if __name__ == '__main__':
    num = int(sys.argv[1])
    tol = float(sys.argv[2])
    print main(num, tol)
