#!/usr/bin/python

#============================================================================
# Project Euler: http://wwww.projecteuler.net
# Problem 7: http://projecteuler.net/index.php?section=problems&id=7
# What is the 10001st prime number?
#============================================================================

#import libraries/modules
import sys
from math import sqrt, floor

#find square root of passed number
def squareRoot(x):
     root = int(floor(sqrt(x)))
     #make the root number odd
     if root % 2 == 0:
          root +=1
     return root

#checks to see if number is prime
def checkPrime(x):
     prime = True   #flag
     
     #basic simple check to see if number passed is even, if it is then it's not a prime number
     if x % 2 == 0: 
          return False
     
     checkedNumber = squareRoot(x)
     for i in range(3,checkedNumber+2,2):
          if x % i == 0:
               prime = False
               break
     return prime

count = 3
primeCount = 2

#main 
while primeCount < 10001:
     count += 2
     if checkPrime(count):
          primeCount +=1
 
print "The 10001 prime number is", count