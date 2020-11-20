import os
import sys
import numpy as np


f=float(sys.argv[1])

def power(x):
    return x**2

def square_root(x):
    return np.sqrt(x)

square=power(f)
root=square_root(f)

print "square result=",square, "root result =",root

for num in range(201):
    print "The top ",num+1 , "is :",num
