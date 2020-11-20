def bmeth(x):
	a=x
	y=0
	while(y!=a):
		y=a
		a=(x/a+a)/2
	return a

print("Babylonian Method")
print("This program calculates the square root of a number using the Babylonian Method")
num=int(input("Give me a positive integer: "))
bab=bmeth(num)
print("The square root of {} is {}".format(num,bab))
