import sys
import math


def newton(a, x):
    return (x + (a/x))/2.0

def square_root(a, x):
    current_x = x
    next_x = newton(a, current_x)
    error = 0.000001
    count = 1
    while abs(next_x - current_x) > error:
        current_x = next_x
        next_x = newton(a, current_x)
        count += 1
        b = next_x * 1.0
    # print "Number of iterations:", count
    # print b


square_root(5, 7000)

sys.stdout.write('{:<3},{:<20},{:<20},{:<20},{:<20}\n'.format('n', "square_root",
                    "math.sqrt", "difference", "is difference < 0.000001?"))
for i in range (0,10):

    sys.stdout.write('{:<3},{:<20},{:<20},{:<20},{:<20}\n'.format(i, math.sqrt(i)))
