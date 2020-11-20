from math import sqrt

# The function square_root takes an integer, a, as a parameter,
# and returns an estimate of the square root of a.
def square_root(a):
    x = a / 2.0
    epsilon = 0.000001
    while True:
        y = (x + (a / x)) / 2.0
        if abs(y - x) < epsilon:
            break
        x = y
    return x

# The function test_square_root compares the value returned from the above square_root
# function to that returned by the sqrt function in the math library.
def test_square_root():
    space = ' ' * 4
    print "%r %s %r %s %r %s %r" % (1.0, space, square_root(1.0), space, sqrt(1.0), space, square_root(1.0) - sqrt(1.0))
    print "%r %s %r %s %r %s %r" % (2.0, space, square_root(2.0), space, sqrt(2.0), space, square_root(2.0) - sqrt(2.0))
    print "%r %s %r %s %r %s %r" % (3.0, space, square_root(3.0), space, sqrt(3.0), space, square_root(3.0) - sqrt(3.0))
    print "%r %s %r %s %r %s %r" % (4.0, space, square_root(4.0), space, sqrt(4.0), space, square_root(4.0) - sqrt(4.0))
    print "%r %s %r %s %r %s %r" % (5.0, space, square_root(5.0), space, sqrt(5.0), space, square_root(5.0) - sqrt(5.0))
    print "%r %s %r %s %r %s %r" % (6.0, space, square_root(6.0), space, sqrt(6.0), space, square_root(6.0) - sqrt(6.0))
    print "%r %s %r %s %r %s %r" % (7.0, space, square_root(7.0), space, sqrt(7.0), space, square_root(7.0) - sqrt(7.0))
    print "%r %s %r %s %r %s %r" % (8.0, space, square_root(8.0), space, sqrt(8.0), space, square_root(8.0) - sqrt(8.0))
    print "%r %s %r %s %r %s %r" % (9.0, space, square_root(9.0), space, sqrt(9.0), space, square_root(9.0) - sqrt(9.0))

