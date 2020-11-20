import itertools
import bisect
import math

_primes = [2, 3, 5, 7]

def _grow_primes():
    n = _primes[-1] + 2
    while not all(n % p for p in _primes):
        n += 2
    _primes.append(n)

def is_prime(n):
    if _primes[-1] < n:
        next_prime(n)
    i = bisect.bisect(_primes, n)
    return _primes[i] is n

def next_prime(n):
    i = bisect.bisect(_primes, n+1)
    if i < len(_primes):
        return _primes[i]
    while _primes[-1] < n:
        _grow_primes()
    return _primes[-1]
    
def square_root_cf(s):
    a0 = int(math.sqrt(s))
    yield a0
    if a0 * a0 == s: return
    a = a0
    m = 0
    d = 1
    while a != 2*a0:
        m = d * a - m
        d = (s - m * m) // d
        a = (a0 + m) // d
        yield a

def convergents(cf_expansion):
    it = iter(cf_expansion)
    p = next(it)
    q = 1    
    p_ = 1
    q_ = 0
    for a in itertools.cycle(it):
        yield p, q
        p_, p = p, a * p + p_
        q_, q = q, a * q + q_

def solve_diophantine(d):
    for x, y in convergents(square_root_cf(d)):
        if x*x - d*y*y == 1:
            return x, y