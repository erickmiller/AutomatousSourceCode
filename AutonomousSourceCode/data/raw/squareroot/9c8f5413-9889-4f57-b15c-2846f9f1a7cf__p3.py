#Find the largest prime factor of a composite number.

import math

def main():
    print largestPrimeFactor(600851475143)

def largestPrimeFactor(n):
    largest = 2
    sqrtN = int(round(math.sqrt(n)))
    for i in xrange(2, sqrtN):
        #print("--" + str(i))
        if n % i == 0 and isPrime(i) and i > largest:
            largest = i
            i = n / largest
    return largest

def isPrime(n):
    squareRoot = round(math.sqrt(n))
    for i in xrange(2, int(squareRoot)):
        if n % i == 0:
            return False
    return True



if __name__ == "__main__":
    main()
