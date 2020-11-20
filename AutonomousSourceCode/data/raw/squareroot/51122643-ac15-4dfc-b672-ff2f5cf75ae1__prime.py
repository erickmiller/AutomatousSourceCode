import math

def is_prime(number, primes=None):
    if number < 2:
        return False

    if primes and number in primes:
        return True

    start_at = 2

    #~ if reduce(lambda x, y: x or (number % y == 0), primes, False):
        #~ return False

    #~ for m in primes:
        #~ foobar = m

    square_root = int(math.sqrt(number))
    if not primes:
        start_at = 2
    else:
        for m in primes:
            if m > square_root:
                break

            if number % m == 0:
                return False

        start_at = m + 1


    for divisor in xrange(start_at, square_root + 1):
        if number % divisor == 0:
            return False

    #~ print "adding: %s" % number
    if primes:
        primes.append(number)
    return True

def gen_primes(max, primes):
    #~ n = 2
    for n in primes:
        if n > max:
            return
        yield n

    if n % 2 != 0:
        n += 1

    for m in xrange(n + 1, max, 2):
        #~ print "testing: %s" % m
        if is_prime(m, primes):
            yield m
