import math 

def triangular(p):
    return (p * (p+1)) / 2

def divisors(p):
    num = 0
    square_root = int(math.ceil(math.sqrt(p))) 
    for x in xrange(1, square_root):
        if p % x == 0:
            num += 2
    if square_root * square_root == p:
        num += 1
    return num    

for x in range(100000):
    t = triangular(x)
    n = divisors(t)
    if n >= 500:
        print t, n
        break
