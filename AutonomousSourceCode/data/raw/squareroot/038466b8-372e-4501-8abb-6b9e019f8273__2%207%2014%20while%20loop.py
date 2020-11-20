# 2/7/14 While Loops

A = 20
B = 5

while A >= B:
    print "A is now", A
    A = A-1

# Calculate square root with while loop

def square_root(N):
    guess = 1.0
    while abs(N - guess**2) > 0.000000000000001:
        quotient = N/guess
        guess = (guess + quotient)/2.0
    return guess

print "The square root of 2 is:", square_root(2)
print "The square root of 4 is", square_root(4)
print "The square root of 25 is:", square_root(25)
print "The square root of 5184 is:", square_root(5184) # 72
print "The square root of 159.283 is:", square_root(159.283) # 12.620
