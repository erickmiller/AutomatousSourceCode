def square(x):
    return x * x


def average(x, y):
    return (x + y) / 2


def improve(guess, x):
    return average(guess, (x / guess))


def good_enough(guess, x):
    return abs(square(guess) - x) < 0.001


def square_root_iter(guess, x):
    if good_enough(guess, x):
        return guess
    else:
        return square_root_iter(improve(guess, x), x)


def square_root(x):
    return square_root_iter(1.0, x)
