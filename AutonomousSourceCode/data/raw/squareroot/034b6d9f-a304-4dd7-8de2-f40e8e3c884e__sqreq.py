__author__ = 'Step'

def bisect(square, left_end=0, right_end=None):
    """
    Square root realisation using bisection method.
    Usage:
    bisect(square, left_end, right_end)
    where square - number from which root is extracted,
    and left_end, right_end are the ends of segment where we're looking for root, optional parameters

    >>> bisect(18)
    4
    >>> bisect(9)
    3
    >>> bisect(100, 0, 50)
    10

    :type square int
    :type left_end int
    :type right_end int
    """

    if square < 0:
        raise ValueError('Cannot extract root of negative number')
    if right_end is None:
        right_end = square
    if right_end - left_end <= 1:
        return rounding_correction(lambda x: x * x - square, [right_end])
    else:
        middle = (right_end + left_end) / 2
        if middle * middle - square < 0:
            return bisect(square, middle, right_end)
        else:
            return bisect(square, left_end, middle)

def rounding_correction(func, roots):
    """
    Last attempt to get rid of rounding errors
    Usage:
    rounding_correction(func, roots), where func is testing function and roots are suspected roots

    >>> rounding_correction(lambda x: x * x - 4, [2])
    2
    >>> rounding_correction(lambda x: x * x - 15, [3])
    4

    Output: list of corrected roots, or root if one.

    :type func function
    :type roots list
    """

    def error(x):
        return abs(func(x))

    roots_testing = map(lambda root: [root - 1, root, root + 1], roots)
    roots_test = map(lambda pot_roots: map(error, pot_roots), roots_testing)

    roots = [roots_testing[i][roots_test[i].index(min(roots_test[i]))] for i in xrange(len(roots))]
    return roots if len(roots) > 1 else roots[0]

def get_roots(a, b, c, discr):
    """
    Main solver

    >>> get_roots(1, -4, 4, 0)
    [2, 2]
    >>> get_roots(50, -225, 253, 25)
    [2, 2]

    :type a int
    :type b int
    :type c int
    :type discr int
    """
    doub_a = a << 1
    sqrt_discr = bisect(discr)
    t1 = - b - sqrt_discr
    t2 = - b + sqrt_discr
    root_l = t1 / doub_a
    root_r = t2 / doub_a

    roots = rounding_correction(lambda x: a * x**2 + b * x + c, [root_l, root_r])
    return roots


def main():
    a, b, c = map(lambda x: int(x), raw_input().split())
    if a == 0 and b == 0 and c == 0:  # checking if solution is all rational numbers
        print -1
        exit()
    if not a:  # checking if equation is linear
        if b:
            print 1
            if not (-b == 2 * c):
                print rounding_correction(lambda x: b * x + c,[- c / b])
            else:
                print 1
        else:
            print 0
        exit()

    # starting to solve quadratic equation
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print 0
    elif not discriminant:
        print 1
        print get_roots(a, b, c, discriminant)[0]
    else:
        print 2
        res = get_roots(a, b, c, discriminant)
        print res[0]
        print res[1]

if __name__ == '__main__':
    main()
