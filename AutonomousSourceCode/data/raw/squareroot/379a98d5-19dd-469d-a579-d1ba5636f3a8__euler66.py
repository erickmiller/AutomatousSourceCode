import math

#this brute method will technically work
#but without any bounds on the answer
#it could theoretically take years or millenia for certain numbers.

def find_x(D):
	y = 1
	test = square_root(1+D*y**2)
	while test*test != (1+D*y**2):
		y+=1
		test = square_root(1+D*y**2)
	return test

#binary search for square roots
#exists due to the fact that for very large numbers,
#(which we won't ever get to, so this is a waste of time)
#the math.sqrt(x) == int(math.sqrt(x)) method won't work.
#however, by the time we get to that point, we're in 10**26
#land, which if we're incrementing by 1, we won't ever get to.
def square_root(x,hi=None,lo=0):
	if x <= 10**26:
		return int(math.floor(math.sqrt(x)))
	if hi == None:
		hi = x
	cur = (hi+lo)/2
	if cur*cur == x:
		return cur
	if hi <= lo:
		return cur
	if cur*cur > x:
		return square_root(x,cur-1,lo)
	if cur*cur < x:
		return square_root(x,hi,cur+1)

def not_square(x):
	root = square_root(x)
	if root * root != x:
		return True
	return False

results = []
for D in filter(not_square,range(1000+1)):
	result = find_x(D)
	results.append(result)
	print D,result
print max(results)
	
