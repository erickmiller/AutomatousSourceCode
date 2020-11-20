import math

'''square root of n will be represented as a tuple (x0,x1,...,x(p-1)), kp
where p is the precision, kp is the rest, i.e. 
n*(10**(p-1))*(10**(p-1)) - xox1...*xox1...
'''

def squareRoot(n,p):
	'''p- precision: the number of digits 
	usable only for n < 100
	return a string'''
	if p == 1: 
		t =  int(math.sqrt(n))
		# print t
		return (str(t),str(n - t*t))

	else:
		t = squareRoot(n,p-1)		
		x = int(t[0])
		k = int(t[1])
		xp = 100*k / (20*x)
		# print 'xp =',xp
		while (20*xp*x + xp*xp) > 100*k:
			xp = xp - 1 
		kp= 100*k - 20*xp*x-xp*xp
		# print t[0],t[1],xp,kp
		return (t[0]+str(xp), str(kp))
print squareRoot(2,10)
print math.sqrt(2)
print squareRoot(3,10)
print math.sqrt(3)
def sumDigits(n,p):
	''' the sum of first p digits of square root of n'''
	t = squareRoot(n,p)
	x= t[0]
	s = 0
	for i in range(0,len(x)):
		s+= int(x[i])
	return s
print sumDigits(2,100)	

def main()	:
	s= 0
	for n in range(2,100):
		t = int(math.sqrt(n))
		if n != t*t:
			print 'attack ', n
			s+= sumDigits(n,100)
	print 'answer',s		
main()	