def squareRootBi(x, epsilon):
    assert x >= 0, "x must be greater than 0"
    assert epsilon > 0, "epsilon must be greater than 0"

    lowBound = 0
    highBound = max(1.0,x)
    guess = (lowBound + highBound)/2.0
    counter = 1
    while abs(guess**2 - x) > epsilon and counter <= 1000:
        if guess**2 < x:
            lowBound = guess
        if guess**2 > x:
            highBound = guess
            
        guess = (lowBound + highBound)/2
        counter += 1
    assert counter <= 1000, "Iteration exceeded"
    print "Square root of x is approximately: " , guess , " Count: " , counter
    return guess

def squareRootNR(x, epsilon):
##    Searching method by Newton-Raphson:
##    Formulae: x(n+1) = x(n) - f(x(n))/f'(x(n))
    assert x >= 0, "x must be greater than 0"
    assert epsilon > 0, "epsilon must be greater than 0"
    
    counter = 1
    x = float(x)
    guess = x/2.0
    diff = guess**2 - x
    while abs(diff) > epsilon and counter <= 1000:
        guess = guess - (diff/(2.0*guess)) #2.0*guess is the derivitive of guess**2
        diff = guess**2 - x
        counter += 1
    assert counter <= 1000, "Iteration exceeded"
    print "Square root of x is approximately: ", guess, " Count: ", counter
    return guess

squareRootBi(123456789,0.01)
squareRootNR(123456789, 0.01)

squareRootBi(123456789,0.0001)
squareRootNR(123456789, 0.0001)

squareRootBi(123456789,0.000001)
squareRootNR(123456789, 0.000001)

squareRootBi(123456789,0.000001)
squareRootNR(123456789, 0.000001)

