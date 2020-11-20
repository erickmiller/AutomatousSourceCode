# http://mathworld.wolfram.com/SchinzelsTheorem.html
# http://en.wikipedia.org/wiki/Lattice_(group)
# http://mathworld.wolfram.com/CircleLatticePoints.html
# http://mathworld.wolfram.com/SquareNumber.html
# http://stackoverflow.com/questions/295579/fastest-way-to-determine-if-an-integers-square-root-is-an-integer

# http://www.mathpages.com/home/kmath265.htm

from math import sqrt

def f(n):
    w = (n // 2) - (1 if n % 2 == 0 else 0)
    r = (n/2)**2
    s = sqrt
    i = 1
    for x in range(1, w) :
        y = s(-x**2 + r)
        if int(y) == y :
            i+=1
            #print(str(x) + "," + str(y))
    return i*4

#print(f(10000))

def f420(n, p):
    w = (n // 2) - (1 if n % 2 == 0 else 0)
    r = (n/2)**2
    s = sqrt
    i = 1
    t = int
    for x in range(1, w) :
        y = s(r - x*x) # is perfect square????
        #y = (r - x*x) ** 0.5
        if t(y) == y :
        #if (r - x*x) % 2:
            i+=1
            #print(str(x) + "," + str(y))
            if i > p :
                return 0
    return i

def prob(d, p):
    p = p // 4
    x = 0
    for n in range(p, d+1):
        if f420(n, p) == p:
            #print(n)
            x+=n
    return x

print(prob(10**4, 420))
