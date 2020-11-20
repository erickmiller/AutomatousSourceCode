#Sum all amicable numbers less than 10000

import math

#Sum of proper divisors of x
def d(x):
    if (x == 0):
        return 0
    
    result = 1
    limit = int(math.floor(math.sqrt(x)))

    #If perfect square subtract square root since it will be counted twice
    if limit*limit == x:
       result -= int(math.sqrt(x))

    for i in range(2,limit + 1):
        if (x % i) == 0:
            result += i
            result += (x/i)   

    return result

def isAmicable(x):
    y = d(x)
    if x == d(y) and x != y:
        return 1
    else:
        return 0



result = 0
for i in range(1,10000):
    if isAmicable(i):
        result += i

print(result)
