#It is found that adding two subsequent odd numbers give square of a number.
# 1+3=4 which is square of 2
#4+5=9 and so on.

# writing a program to compute a entered number square root using this method
#if we have to find square root of 6 we will add first six odds->1+3+5+7+9+11

from __future__ import print_function #to make print finction like print('hi',end=' ') work in python 2.6 and above, for compatibility
import sys

if sys.version_info[0]<3: 
        input=raw_input


def prime_finder(num):
	start_odd=1
	sum=0
	while(num>=1):
		sum=sum+start_odd
		start_odd=start_odd+2
		num=num-1

	return sum

number=input("Enter the number you want to find square of-->")
print("The square of "+number+" is "+ str(prime_finder(int(number))))	
