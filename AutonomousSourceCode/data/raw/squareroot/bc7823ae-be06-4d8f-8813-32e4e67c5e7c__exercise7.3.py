import math

def approx_equal(a, b, limit):
    if abs(a-b) < limit:
        return True
    else:
        return False


def square_root (a):
    x = a / 2.0
    epsilon = 0.001
    while True:
        #print x
        y = (x + a/x) / 2.0
        if approx_equal (y, x, epsilon):
            break
        x = y
    return x
    
def test_square_root(a):
    ex_sqrt = square_root(a)
    py_sqrt = math.sqrt(a)
    diff = abs(ex_sqrt-py_sqrt)
    print a, ex_sqrt, py_sqrt , diff
    
print test_square_root(1.0)
print test_square_root(2.0)
print test_square_root(3.0)
