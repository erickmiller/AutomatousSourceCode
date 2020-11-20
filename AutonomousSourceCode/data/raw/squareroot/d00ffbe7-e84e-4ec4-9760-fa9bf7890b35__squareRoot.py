def sqrt(x):
    ans = 0
    if x >= 0:
        while ans*ans<x: ans = ans + 1
        if ans*ans != x:
            print x, 'is not a perfect square'
            return None
        else: return ans
    else :
        print x, 'is negative number'
        return None


def f(x):
    x = x + 1
    return x


def solve(numLegs, numHeads):
    for numChicks in range(0, numHeads + 1):
        numPigs = numHeads - numChicks
        totLegs = 4*numPigs + 2*numChicks
        if totLegs == numLegs:
            return [numPigs, numChicks]
    print 'Maybe there are some mutants. Dude.'
    return [None, None]

def barnYard():
    heads = int(raw_input('Enter number of heads: '))
    legs = int(raw_input('Enter number of legs: '))
    pigs, chickens = solve(legs, heads)
    if pigs == None:
        print 'There is no solution'
    else:
        print 'Number of pigs:', pigs
        print 'Number of chickens: ', chickens



def isPalindrome(s):
    if len(s) <= 1: return True
    else: return s[0] == s[-1] and isPalindrome(s[1:-1])

def isPalindromel(s, indent):
    print indent, 'isPalindromel called with', s
    if len(s) <= 1:
        print indent, 'About to return True frome this case'
        return True
    else:
        ans * s[0] == s[-1] and isPalindromel(s[1:-1], indent + indent)
        print indent, 'About to return', ans
        return ans


def fib(x):
    if x == 0 or x == 1: return 1
    else: return fib(x-1) + fib(x-2)



def testBi():
    print ' squareRootBi(4, 0.0001)'
    squareRootBi(4, 0.0001)
    print ' squareRootBi(9, 0.0001)'
    squareRootBi(9, 0.0001)
    print ' squareRootBi(2, 0.0001)'
    squareRootBi(2, 0.0001)
    print ' squareRootBi(0.25, 0.0001)'
    squareRootBi(0.25, 0.0001)


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
        #print 'low:', low, 'high:', high, 'guess:', guess
        if guess**2 < x:
            low = guess

        else:
            high = guess
        guess = ( low + high )/2.0
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print 'Bisection method. Num. Iterations:' , ctr, 'Estimate:', guess
    return guess
    
def squareRootNR(x, epsilon):
    """Assume x >= 0 and elsilon > 0
        Return y s.y. y*y is within epsilon of x"""
    assert x >= 0, 'x must be non-negative, not' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    x = float(x)
    guess = x/2.0
    guess = 0.001
    diff = guess**2 - x
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100:
        #print 'Error:', diff, 'guess:', guess
        guess = guess - diff/(2.0*guess)
        diff = guess**2 - x
        ctr += 1
        assert ctr <= 100, 'Iteration count exceeded'
        print 'NR method. Num.. iterations:', ctr, 'Estimated:', guess
        return guess


def compareMethods():
    print ' squareRoot(2, 0.01)'
    squareRootBi(2, 0.01)
    squareRootNR(2, 0.01)
    print ' squareRoot(2, 0.0001)'
    squareRootBi(2, 0.0001)
    squareRootBi(2, 0.0001)com
    
