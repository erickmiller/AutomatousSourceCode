#! env python

# if a ^ 2 + b ^ 2 = c ^ 2
# and a + b + c = s
# then we can write a ^ 2 + b ^ 2 = (s - a - b) ^ 2

from math import sqrt

def hasRoot(x):
    a = x // 2
    seen = set([a])
    while a * a != x:
        a = (a + (x // a)) // 2
        if a in seen:
            return a, False
        seen.add(a)
    return a, True

a = 1
b = 1
found = False
while not found:
    c2 = a ** 2 + b ** 2
    c, isSquare = hasRoot(c2)
    if isSquare:
        if a + b + c == 1000:
            print(a * b * c)
            found = True
    if a + b + c > 1000:
        a += 1
        b = 0
    b += 1
