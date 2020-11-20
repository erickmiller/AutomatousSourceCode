"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import math

def solution(n):

    # use Sieve Theory, creating boolean dict indexed by 2 to n
    sieve = {}
    for i in range(2, n + 1):
        sieve[i] = True

    square_root = int(math.sqrt(n))
    primes = []

    for i in range(2, square_root + 1):
        if sieve[i] == True:
            for j in range(i*i, n + 1, i):
                sieve[j] = False

    for index in sieve:
        if sieve[index] == True:
            print index
            primes.append(index)

    return sum(primes)

print solution(2000000)