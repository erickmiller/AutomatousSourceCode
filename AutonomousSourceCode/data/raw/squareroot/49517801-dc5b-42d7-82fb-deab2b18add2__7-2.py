# Fn. to get the square root of a given value, that takes a as a parameter ,
# that choose a reasonable value of x, and return s an estimate of the squar
# root of a.  
# abs(y - x) < epsilon , that determines how close enough, insteda of using y == x

def sqr_rt(a):
	epsilon = 0.0000001
	x = 3.0
	while True:
		y = (x + a/x) / 2
		if abs(y - x) < epsilon:
			break;
		else:
			x = y

	return y

a = input("Give a number :\n")
result = sqr_rt(a)
print result

