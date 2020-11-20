import math

def square_root(a, x):
    while True:
        y = (x + (a / x)) / 2
        epsilon = 0.0000001
        if abs(y-x) < epsilon:
            return y
            break
        x = y

def test_square_root(a, x):
    print a, ' ', square_root(a, x), ' ', math.sqrt(a), ' ', abs(square_root(a, x) - math.sqrt(a))

test_square_root(1.0, 1.0)
test_square_root(2.0, 2.0)
test_square_root(3.0, 3.0)
test_square_root(4.0, 3.0)
test_square_root(5.0, 3.0)
test_square_root(6.0, 3.0)
test_square_root(7.0, 4.0)
test_square_root(8.0, 4.0)
test_square_root(9.0, 4.0)

