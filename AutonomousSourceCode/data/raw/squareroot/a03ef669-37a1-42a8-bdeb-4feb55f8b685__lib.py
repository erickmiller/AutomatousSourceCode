import math

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    max_divisor = int(n ** 0.5) # square root of n
    divisor = 5
    while divisor <= max_divisor:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True

def factorize(n):
    factors = []

    for x in range(2, int(math.sqrt(n))+1):
        if n%x == 0:
            factors.append(x)
            factors.append(n/x)

    return factors

def chunker(lst, length):
    return (lst[pos:pos+length] for pos in xrange(0, len(lst)))
