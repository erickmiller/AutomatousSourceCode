 def approx_equal(a, b, limit):
    if abs(a-b) < limit:
        return True
    else:
        return False


def square_root (a):
    x = a / 2.0
    epsilon = 0.001
    while True:
        print x
        y = (x + a/x) / 2
        if approx_equal (y, x, epsilon):
            break
        x = y
    return x
    
print square_root(25)

