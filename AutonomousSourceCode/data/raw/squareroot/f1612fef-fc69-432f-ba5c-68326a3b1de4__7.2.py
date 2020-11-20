import math

def square_root(a):
    epsilon = 0.0000001
    if a < 0:
        return 'a must be larger than 0'
    elif a < 1:
        x = 0
    else:
        x = 3**(int(math.log10(a))+1)

    while True:
        y = (x + a / x) / 2.0
        if abs(y-x) < epsilon:
            break
        x = y

    return y

print square_root(4654897)