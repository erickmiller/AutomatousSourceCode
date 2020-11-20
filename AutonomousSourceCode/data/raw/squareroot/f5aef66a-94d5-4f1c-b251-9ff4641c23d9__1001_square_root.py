#!/usr/bin/python

import sys

class Calculator:
  def square_root(self, num, guess=1.0):
    print str(guess)
    if '{:.2f}'.format(guess * guess) == '{:.2f}'.format(num):
      return guess

    return self.square_root(num, (guess + (num / guess)) / 2.0)

calc = Calculator()
number = int(sys.argv[1])
print calc.square_root(number)
