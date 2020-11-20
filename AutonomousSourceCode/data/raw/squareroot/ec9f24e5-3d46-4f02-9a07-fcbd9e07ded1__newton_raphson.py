def square(x): return x * x
def cube(x): return x * square(x)

# First problem
# f(x) = x ^ 3 - 2x - 5
# f`(x) = 3x*2 - 2

def f1(x): 
	return cube(x) - 2 * x - 5

def dfdx1(x):
	return 3 * square(x) - 2


# Second problem
# f(x) = x^6 - 2
# f`(x) = 6x^5

def f2(x):
	return cube(x) * cube(x) - 2

def dfdx2(x):
	return 6 * cube(x) * square(x)

# x is the initial guess
# f is the poly function
# dfdx is the derivative function

def newton_raphson(x, f, dfdx):
	xn = x - ( f(x) / dfdx(x) ) 
	print xn, " ", x
	while(xn > (x + 0.01)):
		newton_raphson(xn, f(xn), dfdx(xn))
	return xn


# xFound = newton_raphson(2, f1, dfdx1)
# print "solution: x = ", xFound


 # expected value of 2.09455, 5 guesses
print newton_raphson(3, f1, dfdx1)
# print newton_raphson(116, f1, dfdx1)


# print (1.2 - (f2(1.2) / dfdx2(1.2)))
# print (1.13395919067 - (f2(1.13395919067) / dfdx2(1.13395919067)))
# print (1.12274956058 - (f2(1.12274956058) / dfdx2(1.12274956058)))
# print (1.12246223231 - (f2(1.12246223231) / dfdx2(1.12246223231)))
# print (1.12246204831 - (f2(1.12246204831) / dfdx2(1.12246204831)))

# print (f1(2) / dfdx1(2))
# print (2 - (f1(2) / dfdx1(2)))
# print (2.1 - (f1(2.1) / dfdx1(2.1)))
# print (2.09456 - (f1(2.09456) / dfdx1(2.09456)))

# print (1 - (f2(1) / dfdx2(1)))
# print (1 - (f2(1) / dfdx2(1)))
# newton_raphson(1, f2, dfdx2) # expected value of 1.122462048309373, 6 guesses
# return the approximate root (when 2 consecutive guesses are the same)
