#!/usr/bin/python

import sys
import math

def isPerfectSquare(n):
	root_n = math.sqrt(n)
	res1 = math.floor(root_n)*math.floor(root_n)
	return (res1 == float(n))

def isFib(n):

	x1 = 5*n*n+4
	x2 = 5*n*n-4

	res1 = isPerfectSquare(x1)
	res2 = isPerfectSquare(x2)

	return ( res1 or res2 )


def main():
	inStream = ''

	#determine in stream(file or stdin)
	if len(sys.argv) < 2:
		inStream = sys.stdin
	else:
		inStream = open('is_fib.in')
	nCases = int(inStream.readline())

	for i in range(0, nCases):
		n = int(inStream.readline())
		result = isFib(n)
		if result:
			print "IsFibo"
		else:
			print "IsNotFibo"


if __name__ == "__main__":
    main()