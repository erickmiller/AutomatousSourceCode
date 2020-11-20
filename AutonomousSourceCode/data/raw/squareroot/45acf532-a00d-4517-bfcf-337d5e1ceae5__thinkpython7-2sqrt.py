#Think Python exercise .2
# estimating square root through newton's method

#The variable assignment is so ugly. maybe figure this out in the future? 
#Don't prematurely optimize. I thought hard already, time to move on
#and I can review later.

def square_root(n):
	"""
		epsilon_constant is used to determine how close the approximation needs to be

	"""
	epsilon_constant = .000001
	x = n
	y = n
	while True:
		x = y
		y = (float(x) + (float(n)/float(x)))/2
		if abs(y-x) < epsilon_constant:
			break
	return y

print (square_root(25))