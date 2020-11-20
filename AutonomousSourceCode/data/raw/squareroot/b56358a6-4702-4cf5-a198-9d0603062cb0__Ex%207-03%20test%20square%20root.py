import math

def squareRoot(a, precision=0.001):
    x = 4.0
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < precision:
            break
        x = y
    
    return y

for i in range(1,10):
    print (str(i) + '\t' + str(squareRoot(i)) + '\t' + str(math.sqrt(i)) + '\t' + str(abs(squareRoot(i)-math.sqrt(i))))