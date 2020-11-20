def squareRootBi(x, epsilon):
    '''Assumes x >= 0, and epsilon > 0
       Return y
    '''
    low = 0
    high = x
    guess = (low + high) / 2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        ctr += 1
    
    
    print "Bi method. Num. iterations:", ctr, "Estimated: ",guess
    return guess
    
    
squareRootBi(100, 5)