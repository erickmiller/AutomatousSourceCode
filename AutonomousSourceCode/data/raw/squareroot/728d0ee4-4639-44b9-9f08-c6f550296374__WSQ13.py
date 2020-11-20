def bmet(x):
	z = x
	y=0
	while (z!=y):
		y=z
		z=((x/z)+z)/2
	return z

print("Babylonian Method.")
x=float(input("Give me the number you want to know the square root."))
print("Square Root: ", bmet(x))
