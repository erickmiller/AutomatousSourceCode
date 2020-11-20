# Find the smallest odd composite that cannot be written as the sum of a prime
# and twice a square

from math import sqrt, floor

def findSpecialComposite():
    listPreviousOddPrime = []
    
    x = 3
    while True:
        if isOddPrime(x, listPreviousOddPrime):
            listPreviousOddPrime.append(x)
        else:
            flagSpecial = False
            # Check if this odd composite can be written as the sum of a prime
            # and twice a square or not
            for oddPrime in listPreviousOddPrime:
                if isSquare((x - oddPrime) // 2):
                    flagSpecial = True
            if flagSpecial == False:
                return x
        
        x += 2
            
            
def isOddPrime(N, listPreviousOddPrime):
    if N <= 2:
        return False
    if not any(listPreviousOddPrime):
        return True

    for divisor in listPreviousOddPrime:
        if N % divisor == 0:
            return False

    return True

def isSquare(N):
    floorSquareRoot = floor(sqrt(N))
    if floorSquareRoot *  floorSquareRoot == N:
        return True
    else:
        return False
