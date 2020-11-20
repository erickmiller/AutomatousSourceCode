def square_root(a, x):
    while True:
        print x
        y = (x + (a / x)) / 2
        epsilon = 0.0000001
        if abs(y-x) < epsilon:
            return y
            break
        x = y

print square_root(4.0, 3.0)

