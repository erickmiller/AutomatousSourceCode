import math

def square_root(a):
    a = float(a)
    x = 10.0
    while True:
        y = (x+a/x)/2
        if abs(y-x)< 0.000000000001:
            break
        x = y
    return x

def layout(m):
    s = str(m)
    return s+' '*(14-len(s))

def printout():
    n = 1
    while n<10:
        n = float(n)
        colOne = square_root(n)
        colTwo = math.sqrt(n)
        diff = abs(colOne-colTwo)
        print (layout(n),)
        print (layout(colOne))
        print (layout(colTwo))
        print (layout(diff))
        n += 1

printout()        
        
