"""When y == x, we can stop. Here is a loop that starts with an
initial estimate, x, and improves it until it stops changing:

while True:
    print x
    y = (x + a/x) / 2
    if y == x:
        break
    x = y

Encapsulate this loop in a function called square_root that takes a as a parameter,
chooses a reasonable value of x, and returns an estimate of the square root of a."""


def square_root(a):
    x = float(a/2)
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x
