from math import sqrt

def sieve(limit):
  primes = [True] * limit
  primes[0] = primes[1] = False

  for (i, is_prime) in enumerate(primes):
    if is_prime:
      yield i
      for n in xrange(i*i, limit, i):
        primes[n] = False

def is_twice_square(num):
  square_root = sqrt(num / 2)
  return square_root == int(square_root)

def P046():
  primes = [_ for _ in sieve(10000)]
  found = True
  i = 1

  while (found):
    found = False
    i += 2
    j = 0

    while (i >= primes[j]):
      if is_twice_square(i - primes[j]):
        found = True
        break
      j += 1

  return i

print P046()