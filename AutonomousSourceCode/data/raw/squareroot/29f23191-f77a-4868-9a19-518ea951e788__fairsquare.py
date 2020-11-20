#!/usr/bin/python

import math

def is_square(apositiveint):
	if(apositiveint==1):
		return True
	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint:
		x = (x + (apositiveint // x)) // 2
		if x in seen:
			return False
		seen.add(x)
	return True

def is_fair(num):
	number=list(str(num))
	length=len(number)
	for i in range(0,length/2+1):
		if(number[i]!=number[length-1-i]):
			return False
	return True

T = int(raw_input())

for case in xrange(1,T+1):
	split=raw_input().split(" ")
	A=long(split[0])
	B=long(split[1])
	count=0
	num=A
	while num<=B:
		if(is_fair(num)):
			if(is_square(num)):
				root = long(math.sqrt(num))
				if(is_fair(root)):
					count = count+1
		num=num+1
	print "Case #"+str(case)+": "+str(count)
		
