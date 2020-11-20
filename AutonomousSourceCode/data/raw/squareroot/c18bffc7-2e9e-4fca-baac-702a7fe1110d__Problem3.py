#! /usr/local/bin/python3.1

from math import sqrt

def isPrime (candidate):
    """
    Determines if candidate is prime or not.
    """
    if ((candidate % 2) == 0):
        if (candidate == 2):
            return True
        else:
            return False

    squareRoot = sqrt(candidate)
    i = 3
    while (i <= squareRoot):
        if ((candidate % i) == 0):
            return False
        i += 2

    return True


number = 600851475143
biggestPrime = sqrt(number)//1
if ((biggestPrime % 2) == 0):
    biggestPrime -= 1

print("Largest prime factor of", number, "is:")

while (biggestPrime > 1):
    if (isPrime(biggestPrime) and ((number % biggestPrime) == 0)):
        print(int(biggestPrime))
        break
    biggestPrime -= 2
