def Sqrt(x, e):
    if x == 0:
        return 0
    # find the square root between i&j
    i,j = 1, x/2+1
    # while error allows
    while j-i >= e :
        c = (i+j)/2
        if c**2 == x:
            return c
        elif c**2 > x:
            j = c - e
        else:
            i = c + e
    return j

print Sqrt(2,0.001)
