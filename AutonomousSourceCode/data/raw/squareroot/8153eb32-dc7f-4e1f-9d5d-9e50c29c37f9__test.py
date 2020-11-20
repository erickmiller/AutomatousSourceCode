def square_root(a):
    x = a / 2.0

    while True:
        y = (x + a / x) / 2

        # You've reached Python's max float precision
        if x == y:
            return x

        x = y

print square_root(32)