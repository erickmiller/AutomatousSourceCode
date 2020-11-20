# Find the largest interger whose square is less than or equal to the given integer. 
# Complexity = O(log n)

def square_root(val):
	l = 0
	u = val

	while (l<=u):
		m = l+(u-l)/2
		
		if (m * m <= val < (m+1)*(m+1)):
			return m
		if (m * m > val):
				u = m-1
		if (m * m < val):
				l = m+1
		
print square_root(81)
print square_root(18)
print square_root(1)
print square_root(0)

