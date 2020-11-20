def squareRootBi(x,epsilon):
    assert x>=0, 'x must be non-negative,not'+str(x)
    assert epsilon>0, 'epsilon must be postive,not'+str(epsilon)
    low=0
    high=max(x,1.0)
    guess=(low+high)/2.0
    ctr=0
    while abs(guess**2-x) > epsilon and ctr <=100:
        #print 'low:',low,'high:',high, 'quess',guess
        if guess**2<x:
            low=guess
        else:
            high=guess
        guess = (low+high)/2.0
        ctr += 1
    assert ctr <= 100,  'Iteration count exceeded' 
    print 'Bi method. Num. iterations', ctr, 'Estimer',guess
    return guess

def testBi():
    print 'squareRootBi(4,0.0001)'
    squareRootBi(4,0.00001)
    print 'squareRootBi(2,0.0001)'
    squareRootBi(2,0.00001)
    print 'squareRootBi(0.25,0.0001)'
    squareRootBi(0.25,0.00001)
