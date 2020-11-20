    # Problem 80: Square root digital expansion

import time, math
t1 = time.clock()

def expand_root(square, precision):
    # Returns the sum of the first y decimal digits for x where y = precision.
    
    digits = []
    c = square
    p = 0
    x = 9
    y = 0
    while len(digits) < precision:
        while True:
            testnum = x*(20*p + x)
            if testnum > c:
                x -= 1
            else:
                y = testnum
                break
        digits.append(x)
        p = p*10 + x
        c = (c-y) * 100
        x = 9
        y = 0
    return sum(digits)

    # Now let's apply the function to each appropriate integer and sum
    # the results!

count = 0
precision = 100
for x in range(2,100):
    if x**.5 % 1 == 0:
        continue
    count += expand_root(x, precision)

print count
            
        
t2 = time.clock()

print "Execution time: ", str(t2-t1)[:5]
