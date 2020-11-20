#!/usr/bin/env python 
# -*- coding: utf-8 -*-

 
############ EJEMPLO 1 ############ 
 
#Don't write what code is doing, this should be left for the code to explain and can be easily done by giving class, variable and method meaningful name. For example:
t=10
#calculates square root of given number 
#using Newton-Raphson method
def abc( a):

  r = a / 2
  while ( abs( r - (a/r) ) > t ):
    r = 0.5 * ( r + (a/r) )

  return r 
 
 
 
 
 
#Above code is calculating square root using Newton-Raphson method and instead of writing comment you can just rename your method and variable as follows:
 
def squareRoot( num):
  root = num/ 2

  while ( abs(root - (num/ root) ) > t ):
    r = 0.5 * (root + (num/ root))

  return root
    
    

if __name__ == "__main__":

  print " root abc = " + str(abc(10))
  print " root squareRoot = " + str(squareRoot(10))


