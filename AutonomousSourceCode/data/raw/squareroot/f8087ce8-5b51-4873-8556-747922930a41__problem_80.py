# -*- coding: utf-8 -*-
'''
  Square root digital expansion
  Problem 80
  It is well known that if the square root of a natural number is not an 
  integer, then it is irrational. The decimal expansion of such square roots is 
  infinite without any repeating pattern at all.

  The square root of two is 1.41421356237309504880..., and the digital sum of 
  the first one hundred decimal digits is 475.

  For the first one hundred natural numbers, find the total of the digital sums 
  of the first one hundred decimal digits for all the irrational square roots.

  Answer: 40886 Completed on Wed, 28 Jan 2015, 20:52
  https://projecteuler.net/problem=80
  
  @author Botu Sun
'''
import math

def sqrt(n, precision_digits=100):
  '''
  Calculate the square root of a integer with high precision.

  Uses digit-by-digit calculation found on:
  http://en.wikipedia.org/wiki/Methods_of_computing_square_roots

  Returns:
    The root with dot and the position of the dot.
  '''
  dot = 0
  count = 0
  root = 0
  current = 0
  while not (current == 0 and n == 0) and count < precision_digits:
    if n == 0:
      current *= 100
    else:
      tmp = n
      i = 0
      while tmp > 100:
        tmp /= 100
        i += 1
      n -= tmp * 100 ** i
      current = current * 100 + tmp
      dot += 1
    # Get trial root
    if root == 0: 
      x = int(math.sqrt(current))
    else:
      x = current / (20 * root)
    # Adjust
    while x * (20 * root + x) > current:
      x -= 1
    current -= x * (20 * root + x)
    root = root * 10 + x
    count += 1
  return root, dot

def sum_of_digits(n):
  sum = 0
  while n != 0:
    sum += n % 10
    n /= 10
  return sum

total = 0
for i in xrange(1, 100):
  if int(math.sqrt(i)) ** 2 != i:
    root, _ = sqrt(i, 100)
    total += sum_of_digits(root)
print total