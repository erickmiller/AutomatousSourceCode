import math

def square_root(a):
    x = a / 2
    epsilon = .000000001
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            return y
        x = y

a = 1.0
print len(str(a))*" "
while a < 10:
    print str(a) + (14 - len(str(a)))*" ",
    res1 = square_root(a)
    print str(res1) + (14 - len(str(res1)))*" ",
    res2 = math.sqrt(a)
    print str(res2) + (14 - len(str(res2)))*" ",
    print abs(res1-res2)
    a += 1
