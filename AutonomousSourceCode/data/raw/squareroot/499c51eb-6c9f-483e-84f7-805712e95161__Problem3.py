    #The prime factors of 13195 are 5, 7, 13 and 29.
    #What is the largest prime factor of the number 600851475143 ?
import math

def isPrime(candidate):
    prime = True
    squareRoot = math.floor(math.sqrt(candidate))
    numbers = range(2, squareRoot)
    divisors = list(filter(lambda x: candidate % x == 0, numbers))
    if len(divisors) != 0 : prime = False

    return prime

max = 600851475143

for x in range(2, max):
    if max % x == 0:
        max /= x
        if isPrime(max):
            print(max)



