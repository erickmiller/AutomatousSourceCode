"""Exercise 7.2. Encapsulate this loop in a function called square_root that takes a as a parameter,
chooses a reasonable value of x, and returns an estimate of the square root of a."""

def my_square_root(a,x) :
    e = 0.0001
    while True :
        y=(x+a/x)/2
        if abs(y-x) < e :
            return y
            break
        x = y

n = 8
import math
for i in range (n):
    a = i+1
    x = i+1    
    c2 = round(my_square_root(float(a),float(x)),3)
    c3 = round(math.sqrt(i+1),3)
    c4 = round(abs(c2-c3),3)
    print(i+1,c2,c3,c4)
    
