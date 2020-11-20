def squareRootBi(x, epsilon):
    """Assume x >= 0 and epsilon > 0
       Return y s.t. y*y is within epsilon of x"""
    assert x >= 0, 'x must be not non-negative, not' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    low = 0
    high = max(x, 1.0)
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        #print 'guess**2 - x is greater than epsilon : ' , epsilon , 'low:', low, 'high:', high, 'guess:', guess
        if guess**2 < x:
            low = guess
            print 'guess**2 - x is less than epsilon : ' , epsilon , ' and now low value is ', low
        else:
            high = guess
            print 'guess**2 - x is greater than epsilon : ', epsilon , ' and now high value is ', high
        guess = ( low + high )/2.0
        print guess
        ctr += 1
        print ctr
    assert ctr <= 100, 'Iteration count exceeded'
    print 'Bisection method. Num. Iterations:' , ctr, 'Estimate:', guess
    return guess


def testBi():
    print ' squareRootBi(4, 0.0001)'
    squareRootBi(4, 0.0001)
    print ' squareRootBi(9, 0.0001)'
    squareRootBi(9, 0.0001)
    print ' squareRootBi(2, 0.0001)'
    squareRootBi(2, 0.0001)
    print ' squareRootBi(0.25, 0.0001)'
    squareRootBi(0.25, 0.0001)
    #In last case, the iteration process is excedded the term 100, so the program stop.


def squareRootNR(x, epsilon):
    """Assume x >= 0 and epsilon >0
        Return y s.t. y*y is within epsilon of x"""
    assert x >= 0, ' x must be non non-negative, not' + str(x)
    assert epsilon > 0, ' epsilon must be positive, not negative'
    x = float(x)
    guess = x/2.0
    guess = 0.0001
    deff = guess**2 - x
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100:
        #print 'Error:', diff, 'Guess: ', guess
        guess = guess - diff/(2.0*guess)
        diff = guess**2 - x
        ctr += 1
        assert ctr <= 100, 'Iteratoin count exceeded'
        print 'NR method. Num. iterations:', ctr,  'Estimate'
     
