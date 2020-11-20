import math

raw_a = raw_input('a = ...\n') 
raw_b = raw_input('b = ...\n') 
a = int(raw_a)
b = int(raw_b)

# function outline (test the return statement)
#def hypotenuse(a,b):
#    return 0.0

# argument validation
#def hypotenuse(a,b):
#    print a
#    print b
#    return 0.0

# compute the sum of argument squares
#def hypotenuse(a,b):
#    print a
#    print b
#    sum = a**2 + b**2
#    print sum
#    return 0.0

# compute square root of the sum
#def hypotenuse(a,b):
#    print a
#    print b
#    sum = a**2 + b**2
#    print sum
#    hypotenuse = math.sqrt(sum)
#    return hypotenuse

# final version (remove scaffolding)
def hypotenuse(a,b):
    sum = a**2 + b**2
    hypotenuse = math.sqrt(sum)
    return hypotenuse

# final version 2 (simplified)
#def hypotenuse(a,b):
#    return math.sqrt(a**2 + b**2)

#print hypotenuse(3,4)
print hypotenuse(a,b)

