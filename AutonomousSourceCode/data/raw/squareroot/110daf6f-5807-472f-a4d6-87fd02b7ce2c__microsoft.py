#return the square root of x
def square(x, delta):
    start = 1
    end = x
    if (x<1):
        start = 0
    sq = float(end+start)/2

    while(abs(sq*sq - x) > delta):
        if (sq*sq > x):
            end = sq
        else:
            start = sq
        sq = (end+start)/2
    return sq

print square(4, 0.001)
print square(5, 0.001)
print square(0.5, 0.001)
print square(0.9, 0.001)