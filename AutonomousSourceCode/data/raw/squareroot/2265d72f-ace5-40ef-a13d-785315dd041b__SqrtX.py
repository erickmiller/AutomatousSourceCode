###Implement int sqrt(int x).

###Compute and return the square root of x.
## (x/2+1)**2 >= x**2
#time O(logn)
#space O(n1)

def Sqrt(x):
	if x == 0:
		return 0
	i = 1
	j = x//2+1
	while (i <= j):
		center = (i+j)//2
		if center**2 == x:
			return center
		elif center **2 >x:
			j = center-1
		else:
			i = center+1
	return j
