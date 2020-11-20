def solve(fvals, x0, debug = False):
    
    x = x0
    n_iter = 0
    tol = 1.e-14
    for h in range(100):
       
        """evaluate function and its derivative:
            """
        fx, fpx = fvals(x)

        if (abs(fx)< tol):
            break
        """update x
            """
        x = x - fx/fpx

    return x, h

def fvals_sqrt(x):
    """
        Return f(x) and f'(x) for applying Newton to find a square root.
        """
    f = x**2 - 4.
    fp = 2.*x
    return f, fp

def test1(debug_solve=False):
    """
        Test Newton iteration for the square root with different initial
        conditions.
        """
    from numpy import sqrt
    for x0 in [1., 2., 100.]:
        print " "  # blank line
        x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print "solve returns x = %22.15e after %i iterations " % (x,iters)
        fx,fpx = fvals_sqrt(x)
        print "the value of f(x) is %22.15e" % fx
        assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x

    
    
	