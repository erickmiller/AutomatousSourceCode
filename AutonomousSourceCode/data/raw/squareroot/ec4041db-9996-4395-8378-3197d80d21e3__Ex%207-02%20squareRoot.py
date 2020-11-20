
def squareRoot(a, precision=0.001):
    x = 4.0
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < precision:
            break
        x = y
    
    return y

print (squareRoot(10))
   
