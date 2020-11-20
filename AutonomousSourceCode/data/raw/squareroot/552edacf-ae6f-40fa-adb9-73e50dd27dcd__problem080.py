#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 080
#

from decorators import benchmark

@benchmark
def solve():
  def root_decimal_expansion(n, limit=10):
    """
    http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Digit-by-digit_calculation
    """
    n = str(int(n))
    if len(n)%2==1: n = '0'+n
    pairs = zip(n[::2], n[1::2])[::-1]
    c = 0
    p = 0
    while pairs or c:
      c *= 100
      if pairs: c += int(''.join(pairs.pop()))
      x = 0
      y = lambda x: x*(20*p + x)
      while y(x+1) <= c: x += 1
      c -= y(x)
      p = 10*p + x 
      if len(str(p)) >= limit:
        break
    return p

  def digital_sum(n, limit=100):
    return reduce(lambda x,y: x+int(y), list(str(root_decimal_expansion(n, limit))), 0)

  perfect_square = [i**2 for i in range(1,11)]
  return sum(digital_sum(i) for i in range(1,101) if i not in perfect_square)

if __name__ == "__main__":
  solve()