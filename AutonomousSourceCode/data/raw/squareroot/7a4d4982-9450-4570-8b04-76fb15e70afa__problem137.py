# Fibonacci golden nuggets
# Problem 137

import time
import math

def solve(max):
    tStart = time.time()
    counter = 0
    for i in range(1,max):
        if isNugget(i):
            counter += 1
            print(i, counter)
    print("Run Time = " + str(time.time() - tStart))
            
            
def isNugget(n):
    return isSquare(5*n*n+2*n+1)
    
def isSquare(n):
    root = int(math.sqrt(n))
    return root*root == n

def fib(n):
    a, b = 1, 1
    for i in range(1,n):
        a, b = a+b, a
    return a