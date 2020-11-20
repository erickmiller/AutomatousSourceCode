#!/usr/bin/env python

import math

class SquareRoot(object):

    epsilon = 1e-12

    @staticmethod
    def sqrt(n):
        if n < 0:
            raise ValueError("sqrt can't be less than 0")

        upper = 1 if n < 1 else n
        lower = 0
        return SquareRoot._sqrt(n, lower, upper)

    @staticmethod
    def _sqrt(n, lower, upper):
        mid = (lower + upper) / 2.0
        midsq = mid * mid

        # base case:
        if abs(midsq - n) < SquareRoot.epsilon:
            return mid

        # recusive case
        if midsq < n:
            return SquareRoot._sqrt(n, mid, upper)
        else:
            return SquareRoot._sqrt(n, lower, mid)

def main():
    print SquareRoot.sqrt(100)
    print SquareRoot.sqrt(0.01)


if __name__ == "__main__":
    main()