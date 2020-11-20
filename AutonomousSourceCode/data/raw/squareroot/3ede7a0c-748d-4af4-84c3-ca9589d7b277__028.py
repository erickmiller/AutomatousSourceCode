"""
Using your knowledge of square roots in addition to standard double precision 
accuracy with your language, what is the square root of the sum of the first 
10^5 square roots?

Enter the number rounded to the nearest whole number
"""
import math

def check_perfect(n):
    return math.floor(math.sqrt(n))**2 == n

res = 0.0

for i in xrange(2, 10**5):
    res += math.sqrt(i)

print res
print math.sqrt(res)