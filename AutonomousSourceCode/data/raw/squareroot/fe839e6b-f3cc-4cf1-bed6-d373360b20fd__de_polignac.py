import math


def polignac(num, p):
    """
    input: num can be any positive integer and p and prime number.

    output: Gives the total number of factors of p in num! (num factorial).
    Stated another way, this function returns the total number of factors
    of p of all numbers between 1 and num; de Polignac's formula is pretty 
    nifty if you are into working with prime numbers.
    """
    factorsDict = {}
    if num > 1 and p == 1:
        print("Invalid entry since 1 is the identity.")
    else:
        while num > 1:
            factorsDict[num // p] = num // p
            num = num // p
        return sum(factorsDict)


def primes():
    '''Yields the sequence of primes via the Sieve of Eratosthenes.'''
    yield 2                 # Only even prime.  Sieve only odd numbers.

    # Generate recursively the sequence of primes up to sqrt(n).
    # Each p from the sequence is used to initiate sieving at p*p.
    roots = primes()
    root = roots.next()
    square = root * root

    # The main sieving loop.
    # We use a hash table D such that D[n]=2p for p a prime factor of n.
    # Each prime p up to sqrt(n) appears once as a value in D, and is
    # moved to successive odd multiples of p as the sieve progresses.
    D = {}
    n = 3
    while True:
        if n >= square:     # Time to include another square?
            D[square] = root + root
            root = roots.next()
            square = root * root

        if n not in D:      # Not witnessed, must be prime.
            yield n
        else:               # Move witness p to next free multiple.
            p = D[n]
            q = n + p
            while q in D:
                q += p
            del D[n]
            D[q] = p
        n += 2


def limite(n, p):
    return(int(math.log(n) / math.log(p)))
print(limite(1000, 3))

MAX = 100

result = {}
for p in primes():
    if p >= MAX:
        break
    lim = limite(MAX, p)
    result[p] = sum(int(MAX / p ** i) for i in range(1, lim + 1))


keys=result.keys()
keys.sort()
for k in keys:
    print(k,result[k])
