__author__ = 'wnduan'

"""
MIT OPEN COURSEWARE
Lecture 6: Bisection methods, Newton/Raphson, introduction to lists
"""

def squareRootBi(x, epsilon):
    """
    Assume x >= 0, and epsilon > 0, Calculates the square root of x
    using bisection method
    :param x: a number >= 0
    :param epsilon: a number > 0, which indicates the accuracy of the result
    :return: square root of x (y s.t. y^2 == x)
    """
    assert x >= 0, 'x must be non-negative, not' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    low = 0.0
    high = max(x, 1.0)
    guess = (low + high)/2.0
    ctr = 0
    while abs(guess**2 - x) > epsilon and ctr < 100:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        ctr += 1
    assert ctr < 100, 'Iteration count exceeded.'
    print 'Bi method, Num. Iterations:', ctr, 'Estimate:', guess
    return guess

def testBi():
    """
    test the function squareRootBi with different input
    :return: None
    """
    print 'squareRootBi(4, 0.0001)'.center(30,'*')
    squareRootBi(4, 0.0001)
    print 'squareRootBi(9, 0.0001)'.center(30,'*')
    squareRootBi(9, 0.0001)
    print 'squareRootBi(2, 0.0001)'.center(30,'*')
    squareRootBi(2, 0.0001)
    print 'squareRootBi(0.25, 0.0001)'.center(30,'*')
    squareRootBi(0.25, 0.0001)

#testBi()
def squareRootNR(x, epsilon):
    """
    Assume x >= 0, and epsilon > 0, Calculates the square root of x
    using Newton-Raphson method.
    :param x: a number >= 0
    :param epsilon: a number > 0, which indicates the accuracy of the result
    :return: square root of x (y s.t. y^2 == x)
    """
    assert x >= 0, 'x must be non-negative, not' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    guess = float(x)/2.0
    # guess = 1
    ctr = 0
    while abs(guess**2 - x) > epsilon and ctr < 100:
        guess = guess - (guess**2 - x)/(2.0*guess)
        ctr += 1
    assert ctr < 100, 'Iteration count exceeded.'
    print 'NR method, Num. Iterations:', ctr, 'Estimate:', guess
    return guess

squareRootNR(3,0.0001)