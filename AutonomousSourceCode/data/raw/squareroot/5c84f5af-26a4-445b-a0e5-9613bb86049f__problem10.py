import math

def problem10(n = 2000000):
	assert(n > 0)
	return sum(generate_primes_upto_number(n))

# generate up to a number or get the first prime
def generate_primes_upto_number(n):
        primes = [2, 3] # first primes
        n -= 1
        current_number = primes[1]
        while current_number < n:
                current_number += 2
                square_root = math.floor(math.sqrt(current_number))
                prime = True
                for p in primes:
                        if p > square_root: break
                        elif current_number % p == 0:
                                prime = False
                                break
 
                if prime: primes.append(current_number)
        return primes