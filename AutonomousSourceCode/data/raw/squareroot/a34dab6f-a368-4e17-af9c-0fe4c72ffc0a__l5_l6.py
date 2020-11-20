def squareRootBi(x,epsilon):
    '''Assumes x >= 0 and epsilon > 0
    Return y such that y*y is within epsilon of x'''

    assert x >= 0, 'x must be positive, not' +str(x)
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    
    low = 0
    high = max(x, 1)
    guess = (low + high)/2.0
    ctr = 1

    while abs(guess**2 - x) > epsilon and ctr <= 100:
        #print 'low:', low, 'high:', high, 'guess:', guess

        if guess**2 < x:
            low = guess
        else:
            high = guess

        guess = (low + high)/2.0
        ctr += 1

    assert ctr <= 100, 'Iteration count exceeded'
    #print 'Bi method. Num. iterations:', ctr, 'Estimate:', guess
    return guess

def testBi():
    print 'squareRootBi(4,0.0001) returns', squareRootBi(4,0.0001)
    print 'squareRootBi(9,0.0001) returns', squareRootBi(9,0.0001)
    print 'squareRootBi(2,0.0001) returns', squareRootBi(2,0.0001)
    print 'squareRootBi(0.25,0.0001) returns', squareRootBi(0.25,0.0001)

def squareRootNR(x, epsilon):
    '''Assumes x >= 0 and epsilon > 0
    Return y such that y*y is within epsilon of x'''

    assert x >= 0, 'x must be positive, not' +str(x)
    assert epsilon > 0, 'epsilon must be positive, not'+str(epsilon)

    x = float(x)
    guess = x/2.0
    #guess = 0.001
    diff = guess**2 - x
    ctr = 1

    while abs(diff) > epsilon and ctr <= 100:
        print 'Error:', diff, 'guess:', guess

        guess = guess - diff/(2.0*guess)
        diff = guess**2 - x
        ctr += 1

    assert ctr <= 100, 'Iteration count exceeded'
    print 'NR method. Num iterations:', ctr, 'Estimate:', guess
    return guess

##Techs = ['MIT', 'Cal Tech']
##print Techs
##Ivys = ['Harvard', 'Yale', 'Brown']
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
##Ivys.remove('Harvard')
##print Univs
##raw_input()
##Ivys[1] = -1
##print Ivys

##L1 = [1,2,3]
##L2 = L1
##L1[0] = 4
##print L2

##L1 = [1,2,3]
##L2 = L1[:] #makes a copy of L1
##L1[0] = 4
##print L2

##L = [['un', 'one'], ['deux', 'two']]
##
##def keySearch(L,k): #goes through nested list L and finds k, returns value adjacent to k
##    for elem in L:
##        if elem[0] == k: return elem[1]
##    return None


##EtoF = {'one':'un', 'soccer': 'football'}
##print EtoF['soccer']
##print EtoF
####print EtoF[0]

##NtoS = {1: 'one', 2: 'two', 'one': 1, 'two': 2}
##print NtoS.keys()
##print NtoS.keys
##del NtoS['one']
##print NtoS
