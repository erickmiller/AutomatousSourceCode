'''
Function for extrcating the
square root
For negative numbers there are no real zeroes
'''

def sqrt2(x,debug=False):
    '''
    square root of a give number
    '''
    if x==0:
        return 0
    elif x<0:
        print "*** Error, x must be non-negative"
        #return 'nan'
    assert x>0. and type(x) is float, "should not get here"
            
    s = 1.
    kmax = 100
    tol = 1.e-14
    for k in range(kmax):
        if debug:
            print "Before iterations %s, s=%20.15f" % (k,s)
        s0 = s
        s = 0.5 * (s + x/s)
        delta_s = s - s0
        #print(delta_s)
        if abs(delta_s / float(x)) < tol:
            break
    if debug:
        print "After iterations %s, s=%20.15f" % (k+1,s)
    return s


