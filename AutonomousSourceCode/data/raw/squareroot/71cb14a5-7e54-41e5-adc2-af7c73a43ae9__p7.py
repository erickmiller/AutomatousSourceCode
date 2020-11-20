#What is the 10 001st prime number?

import math

def main():
    whichPrime = 1
    possiblePrime = 2
    
    while whichPrime < 10001:
        possiblePrime += 1
        
        if isPrime(possiblePrime):
            whichPrime += 1

    print(possiblePrime)


def isPrime(n):
    squareRoot = math.ceil(math.sqrt(n))
    for i in xrange(2, int(squareRoot) + 1):
        if n % i == 0:
            return False
    return True
        
if __name__ == "__main__":
    main()
