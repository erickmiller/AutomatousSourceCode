def square_root(a):
    x = a/2
    epsilon = 0.00000001
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x

#aString = raw_input("What would you like to take the square root of?")
#a = float(aString)

#epString = raw_input("Define error tolerance:")
#epsilon = float(epString)

#print square_root(a, epsilon)

import math

def test_square_root():
    for a in range(1,10):
        a = float(a)
        sqrt = [a, square_root(a), math.sqrt(a), abs(square_root(a) - math.sqrt(a))]
        print '%g \t %g \t %g \t %g \n' %tuple(sqrt)

test_square_root()
