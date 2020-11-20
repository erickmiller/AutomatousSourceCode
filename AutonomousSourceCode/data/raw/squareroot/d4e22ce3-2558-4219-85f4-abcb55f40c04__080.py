#square root algorithm
#http://www.homeschoolmath.net/teaching/square-root-algorithm.php
#http://en.wikipedia.org/wiki/Methods_of_computing_square_roots

from math import sqrt

def sqrt_digit(n): #long division method
    k = n  #remainder
    q = 0  #quotient
    while len(str(q)) < 100:  #check the digits of quotient
        if q == 0:
            temp = q
        else:
            temp = q * 2
        i = 1
        while (temp * 10 + i) * i <= k:
            i += 1
        i = i - 1
        t = (temp * 10 + i) * i  #divider
        q = q * 10 + i
        k = (k - t) * 100  #remainder
    return q

s = 0
for i in xrange(1, 101):
    if sqrt(i) != int(sqrt(i)): #make sure we only add the irrational numbers
        s += sum(map(int, str(sqrt_digit(i))))
    
print s