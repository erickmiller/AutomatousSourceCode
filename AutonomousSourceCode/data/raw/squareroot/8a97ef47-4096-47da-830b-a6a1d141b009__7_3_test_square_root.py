import math

def square_root(a,x):
    """
    a: find the sqrt of a
    x: estimate
    """
    y = (x + a/x)/2
    while abs(y-x)> 0.0000001:
        x = y
        y = (x + a/x)/2
        #print("sqrt:",y)
    return y

def square_root_2(a,x):
    #Using BREAK
    y = (x + a/x)/2
    while True:
        x = y
        y = (x + a/x)/2
        #print("sqrt2:",y)
        if abs(y-x)< 0.0000001:
            break
    return y


def test_square_root():
    a=1.0
    while a<10:
        m = square_root(a,3)
        n = math.sqrt(a)
        print(a,"\t",m,"\t",n,"\t",abs(n-m))
        a = a+1.0

test_square_root()
    
