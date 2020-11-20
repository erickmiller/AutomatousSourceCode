# encoding=utf-8
## SOLVED 2015/01/04
## 40886

# It is well known that if the square root of a natural number is not an
# integer, then it is irrational. The decimal expansion of such square roots is
# infinite without any repeating pattern at all.

# The square root of two is 1.41421356237309504880..., and the digital sum of
# the first one hundred decimal digits is 475.

# For the first one hundred natural numbers, find the total of the digital sums
# of the first one hundred decimal digits for all the irrational square roots.

MAX = 100

# uses the algorithm for digit-by-digit calculation, as described on Wikipedia:
# http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Digit-by-digit_calculation
def euler():
  acc = 0
  # for each starting number
  for c in range(2, MAX):
      acc += square_root_digit_sum(c)
  return acc

# return the sum of the first 100 digits in the irrational square root sqrt(c)
#
# if sqrt(c) is rational, returns 0
def square_root_digit_sum(c):
  # number representing the digits of the root
  p = 0
  i = 0
  # True iff the root is rational
  rational = False
  # for each of the first 100 digits
  while i < 100:
    i += 1
    # calculate the current value for x and y
    x = guess_x(p, c)
    y = x * (20 * p + x)
    # add x as a digit to p
    p = 10 * p + x
    # subtract y from c, and move it two digits to the left
    c -= y
    c *= 100
    # if c is 0, it is rational; just return 0
    if c == 0:
      return 0
  # return the sum of the digits found
  return sum(int(d) for d in str(p))

# helper function for calculating the next digit of the square root
def guess_x(p, c):
  # guess the value of x by "brute force"
  # x is the highest integer that satisfies x(20p + x) <= c, and is going to be
  # the next digit to add to the square root
  x = 1
  while x * (20 * p + x) <= c:
    x += 1
  return x - 1
