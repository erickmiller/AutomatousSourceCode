#!/usr/bin/python 
# Author LavaWong
# Date   7/13/2015 
# Find square root of spec number

#ans = 0
#n = raw_input('Enter a number: ')
#x = int(n)
#while ans*ans < x:
#     ans += 1
#print ans


def sqrt(x):
    if x < 0:
       return None
    ans = 0
    while ans*ans < x:
       ans += 1
    if ans*ans != x:
       print x, ' is not a perfect square root'
       return None
    else:
       print x, ' square root is ', ans
       return ans


n = raw_input('Enter a number: ')
sqrt(int(n))
