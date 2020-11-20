def func(a,n):
    return (
        
        ((a-1)**n)%(a*a),
        ((a+1)**n)%(a*a),
        ((a-1)**n+(a+1)**n)%(a*a)
        )


import math

def primes():
    '''Yields the sequence of primes via the Sieve of Eratosthenes.'''
    yield 2                 # Only even prime.  Sieve only odd numbers.

    # Generate recursively the sequence of primes up to sqrt(n).
    # Each p from the sequence is used to initiate sieving at p*p.
    roots = primes()
    root = roots.next()
    square = root*root

    # The main sieving loop.
    # We use a hash table D such that D[n]=2p for p a prime factor of n.
    # Each prime p up to sqrt(n) appears once as a value in D, and is
    # moved to successive odd multiples of p as the sieve progresses.
    D = {}
    n = 3
    while True:
        if n >= square:     # Time to include another square?
            D[square] = root+root
            root = roots.next()
            square = root*root

        if n not in D:      # Not witnessed, must be prime.
            yield n
        else:               # Move witness p to next free multiple.
            p = D[n]
            q = n+p
            while q in D:
                q += p
            del D[n]
            D[q] = p
        n += 2
prem =primes()
p=prem.next()
print p
n=1
stop=0
while stop <10000000000:
    n+=1
    p=prem.next()
    if n%2==0:
        continue
    stop= 2*n*p
    ##stop=func(p,n)[2]
    print p,n,stop

