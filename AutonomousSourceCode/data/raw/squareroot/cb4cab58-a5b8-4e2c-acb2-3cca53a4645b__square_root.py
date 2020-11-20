import math
# Newton's method
# y = (x + a/x)/2 is always closer to sqr_root of a for any x
epsilon = 0.000000001
# required to calculate the difference between
# 2 floating values because they are unlikely to ever be  exactly the same

def square_root(a):
    global epsilon
    print "epsilon", epsilon
    x = a/2.0 # used 2.0 instead of 2 to make x a float
    y = (x + a/x)/2
    while True:
        if abs(y-x) <= epsilon:
            break
        x = y
        y = (x + a/x)/2
    return x

print square_root(963)
print math.sqrt(963)
print math.sqrt(2)
print square_root(2)
