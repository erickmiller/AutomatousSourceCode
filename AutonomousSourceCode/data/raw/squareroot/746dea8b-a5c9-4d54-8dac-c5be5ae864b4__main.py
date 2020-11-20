# Problem 3: https://projecteuler.net/problem=3
# TODO: this could be cleaned up and checked for correctness even though it gives the correct answer
import math

def IsSquare(apositiveint):
    squareRoot = int(math.sqrt(apositiveint))
    return apositiveint == (squareRoot * squareRoot)

def FermatFactor(N):
    if N % 2 == 0:
        return None

    a = math.ceil(math.sqrt(N))
    b2 = a * a - N

    while b2 > 1 and IsSquare(b2) == False:
        a += 1
        b2 = a*a - N
    return a - math.sqrt(b2), a + math.sqrt(b2)

def largestPrimeFactor(N):
    result = FermatFactor(N)
    if (result != None):
        if result[0] == 1 or result[1] == 1:
            return N

        A = largestPrimeFactor(result[0])
        B = largestPrimeFactor(result[1])

        return max(A, B)

def main():
    print int(largestPrimeFactor(600851475143))

main()
