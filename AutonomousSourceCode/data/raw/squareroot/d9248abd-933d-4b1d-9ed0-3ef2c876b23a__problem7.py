import math
from fractions import gcd
 
def problem7(): return find_prime_by_index(10001)
 
def find_prime_by_index(i):
        return generate_fixed_amount_of_primes(i)[-1]
 
# we do not need to store intermediate primes, but this function can be a good auxiliary function for other euler problems
def generate_fixed_amount_of_primes(n):
        assert(n > 0)
        primes = [2, 3] # first primes
        current_number = primes[1]
        while (len(primes) < n):
                current_number += 2
                square_root = math.floor(math.sqrt(current_number))
                prime = True
                for p in primes:
                        if p > square_root: break
                        elif current_number % p == 0:
                                prime = False
                                break
 
                if prime: primes.append(current_number)
        return primes[:n]