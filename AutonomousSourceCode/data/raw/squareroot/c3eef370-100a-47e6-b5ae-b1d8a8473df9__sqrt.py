# sqrt.py - finding square roots

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

def sqrt(x, error):
    """Returns an approximation to the square root.
        Using Heron of Alexandria's algorithm."""
    guess = 1
    while my_abs(square(guess) - x) > error:
        guess = average(guess, x / guess)
    return guess

#main
print(sqrt(float(input("Square Root of: ")), ERROR))
