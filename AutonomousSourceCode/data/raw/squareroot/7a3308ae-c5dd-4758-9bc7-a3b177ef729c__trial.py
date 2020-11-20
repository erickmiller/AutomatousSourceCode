# Trial division of primes

# Only tests odd numbers from 3 to the square root of a 

def primes_trial(n):
    primes = [2]
    for x in range(2, n+1):
        if all(x % p for p in primes):
            primes.append(x)
    return primes
