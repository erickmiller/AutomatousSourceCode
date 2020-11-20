# newton.py - solving square roots, Newton's way.

DX    = 0.0000001
ERROR = 0.0000001

def main():
    print("*** Newton's Method for Square Roots. ***")
    print("\tEnter '0' to quit.")
    while 1:
        n = float(input("Square Root of: "))
        if not n:
            break
        else:
            root = sqrt(n)
            print(try_as_int(root))

def sqrt(x):
    """Takes a number and returns (an estimate of) the square root.
    Passes a function to newton() and a guess of 1.
    If y is the square root of x then x-y*y = 0."""
    return newton(lambda y: x- y * y, 1) 

def newton(f, guess):
    """Takes a function and a guess.
    Returns the fixed point of Newton's square root method."""
    df = deriv(f)
    return fixed_point(lambda x: x - (f(x) / df(x)), guess)

def deriv(f):
    """Takes a function and returns its derivative."""
    return lambda x: (f(x + DX) - f(x)) / DX

def fixed_point(f, new):
    """Takes a function and a guess. Returns the fixed point of the function."""
    old = 0
    while not close_enough(old, new):
        old, new = new, f(new)
    return new

def try_as_int(x):
    """Takes a number and returns it as an int if it is a whole number."""
    if x % 1 == 0:
        return int(x)
    else:
        return x

def close_enough(u, v):
    """Takes two numbers and returns True if they differ by less than ERROR."""
    return abs(u - v) < ERROR

if __name__ == "__main__":
    main()
