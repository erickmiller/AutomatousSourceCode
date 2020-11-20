# Define f(N) = the sum of squares of divisors of N (N >= 1)
# Find the sum of all n (0 < n < 64 x 10^6 such that f(n) is a perfect square

from math import sqrt, floor

LIMIT = 64000000

def findSumSpecialNum():
    mySum = 0

    sieve = computeSumSquareDivisor()
    print('Hi')
    for x in range(1, LIMIT):
       if isPerfectSquare(sieve[x]):
           mySum += x

    return mySum

def computeSumSquareDivisor():
    # sieve[i] = f(i) = sum of squares of divisors of N >= 1
    sieve = [1] * LIMIT

    sieve[0] = 0

    for x in range(2, LIMIT):
        currentNum = x
        square = x * x

        while currentNum < LIMIT:
            sieve[currentNum] += square
            currentNum += x
            
    return sieve

def isPerfectSquare(N):
    squareRoot = floor(sqrt(N))
    if squareRoot * squareRoot == N:
        return True
    return False


    
