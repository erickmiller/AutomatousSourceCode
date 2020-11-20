# square_root()

def square_root(a):
    '''
    Use x(n+1) = [x(n) + a/x(n)]/2 to calculate square root of a
    '''
    e = 1
    x = a / 2
    while e >= 0.0000001:
        y = (x + a/x) / 2
        e = abs(y-x)
        x = y
    return y


# Test code
print(square_root(1))
