def squareRootBi(x, epsilon=0.0001220703125):
    """Find the square root of x using successive approximation by bissection"""
    assert x >= 0, "x must be greater or equal to 0"
    assert epsilon > 0, "epsilon must be greater than 0"
    low = 0
    # need for rational values, where the root is bigger than x
    high = max(x, 1.0)
    guess = (low + high) / 2.0
    ctr = 1
    while ctr < 100 and abs(guess**2 - x) > epsilon:
        #print("low:", low, "high:", high, "guess", guess)
        if guess**2 > x:
            high = guess
        else:
            low = guess
        guess = (low + high) / 2.0
        ctr += 1
    assert ctr < 100, "shouldn't take more than 100 repetitions to get answer"
    print("Bi Method. Steps:", ctr)
    return guess

def testBi():
    for test in (4, 9, 2, 1024, 13, 0.25):
        print("Testing:", test)
        sq = squareRootBi(test)
        print("Result:", sq)
        print("Diff test - sq**2:", test - sq**2)
        print()

def squareRootNR(x, epsilon=0.0001220703125):
    """Find the square root of x using Newton/Raphson method"""
    assert x >= 0, "x must be greater or equal to 0"
    assert epsilon > 0, "epsilon must be greater than 0"
    guess = 1
    diff = guess**2 - x
    ctr = 1
    while ctr < 100 and abs(diff) > epsilon:
        guess = guess - diff/(2.0 * guess)
        diff = guess**2 - x
        ctr += 1
    assert ctr < 100, "shouldn't take more than 100 repetitions to get answer"
    print("NR Method. Steps:", ctr)
    return guess

def testNR():
    for test in (4, 9, 2, 1024, 13, 0.25):
        print("Testing:", test)
        sq = squareRootNR(test)
        print("Result:", sq)
        print("Diff test - sq**2:", test - sq**2)
        print()

def testBoth():
    for test in (4, 9, 2, 1024, 13, 0.25, 123456789):
        print("Testing:", test)
        sqNR = squareRootNR(test)
        sqBI = squareRootBi(test)
        print("Results NR:", sqNR, "BI:", sqBI)
        print()

#testBi()
#testNR()
testBoth()
