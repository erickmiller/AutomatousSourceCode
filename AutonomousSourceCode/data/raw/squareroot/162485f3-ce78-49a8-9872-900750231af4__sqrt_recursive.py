# sqrt_recursive.py - finding square roots

ERROR = 0.0000000001

def square(x):
    """Returns the square of a number."""
    return x*x

def average(x,y):
    """Returns the average of two numbers."""
    return (x + y) / 2

def my_abs(x):
    """Returns the absolute value of x."""
    if x < 0:
        return -x
    else:
        return x

def sqrt(x, guess, error):
    """Recursive version."""
    if my_abs(square(guess) - x) < error:
        return guess
    else:
        return sqrt(x, average(guess, x / guess), error)

#main
print(sqrt(float(input("Square Root of: ")), 1, ERROR))
