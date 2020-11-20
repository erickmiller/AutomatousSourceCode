"""
Clifton Crosland
Project Euler 80 - Summing the digits of irrational square roots
Source of the square roots algorithm: http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
"""

import math

def make_groups_of_two(n):
  str_n = str(n)
  if len(str_n) % 2 == 1:
    # Append leading zero if necessary
    str_n = "0" + str_n
  groups = []
  i = 0
  while i < len(str_n):
    groups.append(str_n[i:i+2])
    i += 2
  groups += ["00"] * (100 - len(groups)) # We want first 100 digits of square roots
  return groups

def sum_of_digits(n):
  total = 0
  while n != 0:
    total += n % 10
    n /= 10
  return total

# Guess and check
def get_best_x(c, p):
  for x in range(0, 11):
    if (20 * p + x) * x > c:
      return x-1
  print "ERROR! NO DIGITS WORK!"
  return -1 # ERROR

# Precondition: Square root of n is not an integer (hence, root is irrational)
def sum_of_100_digits_of_irr_root(n):
  n_groups = make_groups_of_two(n)
  result = 0
  remainder = 0
  for group in n_groups:
    c = remainder * 100 + int(group)
    x = get_best_x(c, result)
    remainder = c - (20*result + x) * x
    result = result * 10 + x
  return sum_of_digits(result)
  
def main():
  squares = [1,4,9,16,25,36,49,64,81,100]
  total = 0
  for i in range(1, 101):
    if i not in squares:
      total += sum_of_100_digits_of_irr_root(i)
  print total
  
if __name__ == "__main__":
  main()