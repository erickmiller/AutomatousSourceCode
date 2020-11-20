##def squareRootBi(x, epsilon):
##    """Return y s.t. y*y is within epsilon of x"""
##    assert epsilon > 0, 'epsilon must be postive, not' + str(epsilon)
##    low = 0
##    high = max(x,1)
##    guess = (low + high)/2.0
##    ctr = 1
##    while abs(guess**2 - x) > epsilon and ctr <= 100:
##        #print 'low:', low, 'high:', high, 'guess:', guess
##        if guess**2 < x:
##            low = guess
##        else:
##            high = guess
##        guess = (low + high)/2.0
##        ctr += 1
##        assert ctr <= 100, 'Iteration count exceeded'
##    print 'Bi method. Num. iterations:', ctr, 'Estimate:', guess
##    return guess
##
##def TestBi():
##    print 'square root with 4 and 0.001'
##    squareRootBi(4,0.001)
##    print 'square root with 2 and 0.001'
##    squareRootBi(2,0.001)
##    print 'square root with 0.25 and 0.001'
##    squareRootBi(0.25,0.001)
##
##    return None
##
##def TestNR():
##    print 'square root with 4 and 0.001'
##    squareRootNR(4,0.001)
##    print 'square root with 2 and 0.001'
##    squareRootNR(2,0.001)
##    print 'square root with 0.25 and 0.001'
##    squareRootNR(0.25,0.001)
##
##    return None
##
##def squareRootNR(x, epsilon):
##    """Assumes x >= 0 and epsilon > 0
##    Return y s.t. y*y is within epsilon of x"""
##    assert x >= 0, 'x must be non-negative, not' + str(x)
##    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
##    x = float(x)
##    guess = x/2.0
##    guess = 0.001
##    diff = guess**2 -x
##    ctr = 1
##    while abs(diff) > epsilon and ctr <= 100:
##        #print 'Error:', diff, 'guess:', guess
##        guess = guess - diff/(2.0*guess)
##        diff = guess**2 -x
##        ctr += 1
##    assert ctr <= 100, 'Iteration count exceeded'
##    print 'NR method. Num. iterations:', ctr, 'Estimate:', guess
##    return guess
##
##def compareMethods():
##    print 'square root with 4 and 0.001'
##    squareRootBi(4,0.001)
##    squareRootNR(4,0.001)
##    
##
##    print 'square root with 9 and 0.001'
##    squareRootBi(9,0.001)
##    squareRootNR(9,0.001)
##
##    
##    print 'square root with 2 and 0.001'
##    squareRootBi(2,0.001)
##    squareRootNR(2,0.001)
##    
##
##    print 'square root with 2 and 0.0001'
##    squareRootBi(2,0.0001)
##    squareRootNR(2,0.0001)
##    
##
##    print 'square root with 2 and 0.000001'
##    squareRootBi(2,0.000001)
##    squareRootNR(2,0.000001)
##    
##
##    print 'square root with 0.25 and 0.001'
##    squareRootBi(0.25,0.001)
##    squareRootNR(0.25,0.001)
##
##    print 'square root with 123456789 and 0.0001'
##    squareRootBi(123456789,0.0001)
##    squareRootNR(123456789,0.0001)
##
##    print 'square root with 123456789 and 0.000001'
##    squareRootBi(123456789,0.0000001)
##    squareRootNR(123456789,0.000001)
##
##compareMethods()
##
Techs = ['MIT', 'Cal Tech']
##print Techs

Ivys = ['Harvard', 'Yale', 'Brown']
##print Ivys
##Univs = []
##Univs.append(Techs)
##print Univs
##Univs.append(Ivys)
##raw_input()
##print Univs
##raw_input()
##for e in Univs:
##    print e
##    for c in e: print c
##raw_input()
##Univs = Techs + Ivys
##print Univs
##
##Ivys.remove('Harvard')
##print Univs ##univs will not have changed
##
## this shows that lists can show mutation
####
####
