#!/usr/bin/python

import sys

class Calculator:
    def square_root_bisection(self, num):
        epsilon = 0.01
        num_guesses = 0
        low = 0.0
        high = num
        ans = (high + low) / 2.0

        while abs(ans**2 - num) >= epsilon:
            num_guesses += 1
            if ans**2 < num:
                low = ans
            else:
                high = ans
            ans = (high + low) / 2.0

        return ans

calc = Calculator()
number = int(sys.argv[1])
print calc.square_root_bisection(number) 
