import sys
from math import sqrt

def pal(value):
	s = str(value)
	s = s.split(".")[0]
	return (s == s[::-1])

def is_square(integer):
	root = isqrt(integer)
	l = root*root
	if l == integer:
		return pal(root)
	else:
		return False

'''
def is_square(integer):
	root = sqrt(integer)
	if root.is_integer():
		return pal(root)
	else:
		return False
'''
def isqrt(n):  
	xn = 1  
	xn1 = (xn + n/xn)/2  
	while abs(xn1 - xn) > 1:  
		xn = xn1  
		xn1 = (xn + n/xn)/2  
	while xn1*xn1 > n:  
		xn1 -= 1  
	return xn1  


def sqrt1(n, precision=10e-8):
	prev, mid = 0, float(n)
	while abs(mid - prev) > precision:
		prev, mid = mid, (mid + (n / mid)) / 2.0
	return mid

def binsqrt(n):
	sgn = 0
	if n < 0:
		n = -n
		sgn = -1
	low = 0.0
	upp = n
	mid = (low + upp) * 0.5
	while True:
		if mid * mid > n:
			upp = mid
		else:
			low = mid
		last = mid
		mid = (upp + low) * 0.5
		if abs(mid - last) < 1e-9:
			break
	if sgn < 0:
		return complex(0, mid)
	return mid
 

def ntsqrt(n):
	if n < 10000000:
		return sqrt(n)
	sgn = 0
	if n < 0:
		sgn = -1
		n = -n
	val = n
	while True:
		last = val
		val = (val + n / val) * 0.5
		if abs(val - last) < 1e-9:
			break
		if sgn < 0:
			return complex(0, val)
	return val

my_file = open(sys.argv[1], 'r')

tests = int(my_file.readline())

for i in range(tests):
	tx = ((my_file.readline()).rstrip('\n')).split(" ")
	A=long(tx[0])
	B=long(tx[1])
	results = 0

	for v in range(A,B+1):
		if pal(v):
			if is_square(v):
				results +=1

	print "Case #{0}: {1}".format((i+1),results)


