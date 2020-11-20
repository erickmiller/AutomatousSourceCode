import math

def harmonic():
    total = 0
    for k in range (10, ((10**7)+1), 10):
        print (k, "= ",(1/(k**2)))
        total += (1/(k**2))
    print ("the square root of 6 * the sum =", math.sqrt(total * 6))
    #return total

def main():
    harmonic()

    #n = int(input("enter positive integer"))
    #print('The sum of 1/k**2 for k =1 to', n, "is ", harmonic(n))
    #print (the square root of 6 * the sum of 1/k**2)

main()