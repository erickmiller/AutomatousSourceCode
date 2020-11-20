import math

def is_square(x):
    root = (int)(math.sqrt(x))
    return x == root ** 2

def int_area(s, b):
    if b % 2 != 0:
        return False
    if is_square(s ** 2 - (b/2) ** 2) == False:
        return False
    return True

def perim(s, b):
    return s * 2 + b

perim_sum = 0
side = 3
while (side <= 1000):
    if int_area(side, side+1):
        print side, side + 1
        perim_sum += perim(side, side+1)
        side*=3
    elif int_area(side, side-1):
        print side, side - 1
        perim_sum += perim(side, side-1)
        side*=3
    side+=2
print perim_sum
