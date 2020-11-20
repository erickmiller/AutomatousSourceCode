import math

anumber = int(input("Enter an integer: "))
try:
	print(math.sqrt(anumber))
except:
	print("Bad value for square root")
	print("Using absolute value instead")
	print(math.sqrt(abs(anumber)))

anumber = int(input("Enter an integer: "))
if anumber < 0:
	raise RuntimeError("You can't use a negative number")
else:
	print(math.sqrt(anumber))

def cube(n):
	return n ** 3
print(cube(anumber))

def squaeroot(n):
	root = n/2
	for k in range(20):
		root = (1/2)*(root + (n / root))
	return root

print(squaeroot(anumber))

input("Press Enter")