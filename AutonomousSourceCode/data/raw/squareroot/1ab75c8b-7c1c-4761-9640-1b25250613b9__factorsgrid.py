#!/usr/bin/python

import random

# cool grid pattern about prime factors
# each cell is sum of the cell above and cell to the left 
# HOWEVER no number can exist that has multiple of the same prime factor
# if this would happen then you have to automatically take out all duplciate 
# copies of this factor
# Eg 12 reduces to 6

def genGrid(rows, cols):
    initVal = 0
    grid = [[initVal for r in range(rows)] for c in range(cols)]
    setStartingVals(grid)
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            # Skip custom starting condition cells
            if val != initVal:
                continue

            upVal = 0
            if r != 0:
                upVal = grid[r-1][c]

            leftVal = 0
            if c != 0:
                leftVal = grid[r][c-1]

            sum = upVal + leftVal
            grid[r][c] = removeDuplicateFactors(sum)

    return grid

def setStartingVals(grid):
    grid[0][1] = removeDuplicateFactors(random.randrange(1000))
    grid[1][0] = removeDuplicateFactors(random.randrange(1000))

# Returns largest squarefree multiple of n
def removeDuplicateFactors(n):
    factors = primeFactors(n)
    uniqueFactors = []
    for factor in factors:
        if factor not in uniqueFactors:
            uniqueFactors.append(factor)
    product = reduce(lambda x,y: x*y, uniqueFactors, 1)
    return product

def primeFactors(n):
    factors = []
    remaining = n
    while True:
        # TODO could optimize speed by not calling firstPF() in a loop. 
        # Because this re-searches the low primes over and over
        # Also could memoize list of low primes, etc. 
        nextFactor = firstPrimeFactor(remaining)
        # If no next factor found, we are done.
        if nextFactor <= 0:
            return factors

        # Else save the factor, shrink 'remaining', and proceed
        factors.append(nextFactor)
        remaining = remaining / nextFactor

def isPrime(n):
    return firstPrimeFactor(n) == n

def firstPrimeFactor(n):
    if n < 2:
        return -1

    candidate = 2
    while candidate * candidate <= n:
        if n % candidate == 0:
            return candidate

        # Increment to next candidate factor.
        while True:
            # Go to next odd number, ie +2 unless we're at 2.
            if candidate == 2:
                candidate = 3
            else:
                candidate = candidate + 2

            if isPrime(candidate) or candidate**2 > n:
                break

    # Case where n is prime
    return n

def printGrid(grid):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val <= 9999:
                print("{:4d}".format(val)),
            else:
                print("XXXX"),
        print("")

# 1 does not count. 
# If n is squarefree, returns 1
def firstSquareFactor(n):
    root = 2
    square = root * root
    while square <= n:
        if n % square == 0:
            return square
        root = root + 1
        square = root * root
    return 1


# Are any of the factors of n perfect squares? (not counting 1 obviously)
def isSquareful(n):
    return firstSquareFactor(n) != 1

# 'for a given range, what is the ratio of squareful to squarefree integers?'
def printSurvey(start, count):
    for i in range(start, start + count):
        if isSquareful(i):
            print(str(i) + ' has a square factor')
        else:
            print(str(i) + ' does not have a square factor')




# commands for 'python factorsgrid.py'
# printSurvey(25129935713329319, 50)

# 42,56 fits my screen (2015 july 2 at 1248)
#printGrid(genGrid(42,56))

