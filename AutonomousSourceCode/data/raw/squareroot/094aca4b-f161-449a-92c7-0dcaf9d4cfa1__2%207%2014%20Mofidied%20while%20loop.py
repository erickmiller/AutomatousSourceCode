# Modified 2/7/14

# Can't skip any of these, must give N, then accuracy if you want, then guess
def square_root(N, accuracy=0.000001, guess=1.0):
    
    while abs(N - guess**2) > accuracy:
        quotient = N / guess
        guess = (guess + quotient)/2.0
    return guess

print "The square root of 2 is:", square_root(2)
print "The square root of 2 is:", square_root(2, 0.001)
print "The square root of 4 is:", square_root(4, 0.000001)
print "The square root of 25 is:", square_root(25, 0.0002)
print "The square root of 1000 is:", square_root(1000, 0.01, 30)
print "The square root of 2000 is:", square_root(2000, guess=35)
print "The square root of 3000 is:", square_root(3000, guess=40, accuracy=0.01)
