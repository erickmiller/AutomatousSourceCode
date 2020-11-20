'''
Created on Jan 17, 2013

@author: PaymahnMoghadasian
'''
from numpy.ma.core import floor

number = 600851475143
primes = []
factors = []

def find_primes(n):
    '''Find all primes <= n'''
    for i in range(20, n):
        if is_prime(i):
            primes.append(i)

def is_prime(n):
    '''Checks to see if n is prime'''
    root = n ** 0.5
    for i in primes:
    # for i in range(2, int(root) + 1):
        if n % i == 0:
            return False
        if i > root:
            return True
        
    return True

def find_largest_prime_factor(n):
    while n > 2:
        for i in primes:
            if n % i == 0 and i not in factors:
                factors.append(i)
                n /= i
                break

square_root = number ** 0.5
find_primes(int(square_root) + 1)
find_largest_prime_factor(number)

print factors[-1]


