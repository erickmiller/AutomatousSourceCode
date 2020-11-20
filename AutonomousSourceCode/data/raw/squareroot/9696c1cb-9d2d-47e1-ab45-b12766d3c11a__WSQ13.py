def babylonian(x):
	c=x
	y=0
	while(y!=c):
		y=c
		c=(x/c+c)/2
	return c

a= int(input("Write a number"))

b= babylonian(a)

print("The square root is", b)
