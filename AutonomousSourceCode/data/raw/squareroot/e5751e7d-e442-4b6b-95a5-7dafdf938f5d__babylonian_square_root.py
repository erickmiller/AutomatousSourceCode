# import appropriate modules/libraries
from sys import argv

# define Babylonian Algorithm used in finding root
def bab(n,r):
	return 0.5*(n+r/n)

# find roots
def find_root(x):	
	eps=1e-11
	root = x
	while(abs(root-bab(root,x))>eps):
		root = bab(root,x)
	return root 

# return results
i = 1
while (i < len(argv)):
	print "The square root of", argv[i], "is", find_root(int(argv[i]))
	i = i + 1
	