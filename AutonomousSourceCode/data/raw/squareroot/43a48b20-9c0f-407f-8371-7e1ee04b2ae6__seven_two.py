def square_root(a, x):
    """returns the square root of the number using newton's method
       other parameter is a valid integer """
    for i in range(5):
        y = (x + a / x) / 2
        x = y
    return y
"""i imported it elsewhere so i made this test code execute
only when script is executed"""
if __name__ == '__main__':
    print "{0:.20f}" .format(square_root(9.0, 6))
