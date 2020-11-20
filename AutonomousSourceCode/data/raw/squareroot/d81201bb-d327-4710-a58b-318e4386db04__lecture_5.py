# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 15:48:18 2014

@author: Sifan
"""

def squareRootBi(x,epsilon):
    '''
    Assume x>=0 and epsilon > 0, 
    Return y s.t. y*y is within epsilon of x.
    '''
    assert x >= 0, 'x must be non-negative, not' + str(x)
    assert epsilon > 0, 'epsilon must greater than ZERO, not' + str(epsilon)
    low = 0
    # high = x
    high = max(x, 1.0)        # 注意这里将原来的 high=x 改为 max(x,1.0)
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print 'Bi Method.  Num. of Iteration:', ctr, ' Estimation:', guess
    return guess
    
def testBi():
    print '   squareRootBi(4, 0.0001)'
    squareRootBi(4,0.0001)
    print '   squareRootBi(9, 0.0001)'
    squareRootBi(9,0.0001)
    print '   squareRootBi(2, 0.0001)'
    squareRootBi(2,0.0001)
    print '   squareRootBi(0.25, 0.0001)'
    squareRootBi(0.25,0.0001)
    print '   squareRootBi(0.75, 0.0001)'
    squareRootBi(0.75,0.0001)

def squareRootNR(x,epsilon):
    '''
    Assume x >= 0 and epsilon > 0,
    Return y s.t. y**2 is within epsilon of x.
    '''
    assert x >=0, 'x must be non-negative, not' + str(x)
    assert epsilon > 0, 'epsilon must greater than ZERO, not' + str(epsilon)
    x = float(x)
    guess = x / 2.0
    # guess = 0.01
    diff = guess**2 - x
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100:
        # print 'guess=', guess, 'diff=', diff, 'ctr=', ctr
        guess = guess - diff/(2*guess)
        diff = guess**2 - x
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print 'NR Method.  Num. of Iteration:', ctr, ' Estimation:', guess
    return guess

def test_compareMethods():
    print '   squareRoot(2, 0.01)'
    squareRootBi(2, 0.01)
    squareRootNR(2, 0.01)
    raw_input()
    print '   squareRoot(2, 0.0001)'
    squareRootBi(2, 0.0001)
    squareRootNR(2, 0.0001)
    raw_input()
    print '   squareRoot(2, 0.000001)'
    squareRootBi(2, 0.000001)
    squareRootNR(2, 0.000001)
    raw_input()
    print '   squareRoot(123456789, 0.0001)'
    squareRootBi(123456789, 0.0001)
    squareRootNR(123456789, 0.0001)
    raw_input()
    print '   squareRoot(123456789, 0.0000001)'
    squareRootBi(123456789, 0.0000001)
    squareRootNR(123456789, 0.0000001)
    raw_input()

def addthe2(x,y):
    return x + y

def printntimes(s,n):
    for i in range(n):
        print s

#printntimes(addthe2('Stefan', 'Duan'),5)

def right_justify(s):
    length = len(s)
    spaces = ' ' * (70 - length)
    print spaces + s
    
#right_justify("South China University")
#right_justify("of Technology")
#right_justify("Duan Weining")
#right_justify("2014.10.29")

def cal(f,x):
    return f(x,0.0001)