def is_prime(i):
    """ function to determine whether an integer is a prime number or not"""
    if i == 1:
        return False
    for divisor in range (2, int(i**0.5)+1):
        if i % divisor == 0: 
            return False
    return True

def largestprime(x):
    factor = 0
    # check for prime number up till square root of x
    for i in range(1,int(x**0.5) +1):
        if x % i == 0 and is_prime(i):
            factor = i
    print(factor)

largestprime(600851475143)
    
