import numpy
import time
import math
start_time = time.time()

def get_primes(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n / 3 + (n % 6 == 2), dtype=numpy.bool)
    for i in xrange(1, int(n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k / 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]


lim = 10 ** 50
root = lim ** 0.5
primes = get_primes(int(math.sqrt(lim))+1)

squares = set()
for i in primes:
    if primes[i] > root:
        break
    square = j = primes[i] ** 2
    while j < lim:
        squares.add(j)
        j += square

print len(squares)
print 2 ** 50 - len(squares)

print 'Seconds', time.time() - start_time
