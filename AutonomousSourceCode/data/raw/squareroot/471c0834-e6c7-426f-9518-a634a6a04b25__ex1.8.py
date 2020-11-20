def cube(x):
    return x*x*x

def square(x):
    return x * x

def cube_root_iter(guess, x):
    if is_good_enough(guess, x):
        return guess
    else:
        return cube_root_iter(improve(guess, x), x)

def improve(guess, x):
    return (x/square(guess) + (2 * guess)) / 3

def is_good_enough(guess, x):
    return abs(cube(guess) - x) < 0.001

def cube_root(x):
    return cube_root_iter(1.0, x)
