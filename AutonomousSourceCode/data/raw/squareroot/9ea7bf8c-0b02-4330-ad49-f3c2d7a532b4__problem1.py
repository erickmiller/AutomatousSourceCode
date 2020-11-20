'''
Problem:
  Given a positive integer n, determine whether it is prime using trial
  division by all primes not exceeding its square root.

Constraints:
  n - must be a positive integer
'''

def problem(n):
  if (n < 1):
    raise ValueError("n must be a positive integer")
  elif (n == 1):
    return True
  elif (n == 2):
    return False

  square_root = int(n ** .5)

  for i in xrange(0, square_root + 1):
    if (isPrime(i)):
      if (n % i == 0):
        return True

  return False

# Trivial prime checker
def isPrime(n):
  if (n <= 1):
    return False
  elif (n == 2):
    return True
  elif (n % 2 == 0):
    return False

  sqrt = int(n ** .5) + 1

  i = 3

  while i < sqrt:
    if (n % i == 0):
      return False

  return True
