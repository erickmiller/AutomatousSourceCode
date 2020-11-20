"""This function will approximate the square root of a number using Newton's Method"""

x = float(input("Enter a positive number and I will find the square root: "))

def square_root(x):
    y = x/2
    count = 0
    while abs((y**2) - x) > 0.01:
        y = (y+x/y)/2
        count += 1
        print("After iterating {} times, my guess is {}.".format(count, y))
    return y
print("The square root of {} is {}.".format(x, square_root(x)))
