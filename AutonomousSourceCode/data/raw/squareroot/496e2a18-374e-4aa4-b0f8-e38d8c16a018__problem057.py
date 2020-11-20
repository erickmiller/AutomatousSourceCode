#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 57
#
# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
#
# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + … ))) = 1.414213…
#
# By expanding this for the first four iterations, we get:
#
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666…
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379…
#
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first 
# example where the number of digits in the numerator exceeds the number of digits in the denominator.
#
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

from decorators import benchmark
from fractions import Fraction

def brute_force():
  # brute force recursion
  def two_square_root(expansion=1):
    def decimal_part(expansion):
      if expansion <= 1:
        return Fraction(1,2)
      return 1/Fraction(2 + decimal_part(expansion-1))
    return Fraction(1 + decimal_part(expansion))

  # good but breaks with two many recursion
  s = 0
  for i in xrange(1,1000):
    f = two_square_root(i)
    if len(str(f.numerator)) > len(str(f.denominator)):
      s += 1
  return s

# smart generator
@benchmark
def smart():
  def tw_square_root_gen(limit=100):
    i,r = 0, 1+Fraction(1,2)
    while i < limit:
      yield r
      r = 1+1/(1+r)
      i += 1

  s = 0
  for f in tw_square_root_gen(1001):
    if len(str(f.numerator)) > len(str(f.denominator)):
      s += 1
  return s

if __name__ == "__main__":
  smart()