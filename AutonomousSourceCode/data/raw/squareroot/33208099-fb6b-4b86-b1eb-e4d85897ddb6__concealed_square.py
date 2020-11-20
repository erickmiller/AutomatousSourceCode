#!/usr/bin/python

# Solution for Project Euler problem 206, "Concealed Square".
# http://projecteuler.net/problem=206

import math

def solve():
  lower = int(math.sqrt(1020304050607080900))
  upper = int(math.ceil(math.sqrt(1929394959697989990)))

  # Root must end in 30 or 70 (see README). Skip iterating over other numbers.
  for x in xrange(lower - (lower % 100), upper + 100 - (upper % 100), 100):
    if attempt(x + 30): return x + 30
    if attempt(x + 70): return x + 70

def attempt(n):
  sq = n*n
  return odd_digits(sq) == '1234567890'

def odd_digits(n):
  return str(n)[0::2]

print solve()
