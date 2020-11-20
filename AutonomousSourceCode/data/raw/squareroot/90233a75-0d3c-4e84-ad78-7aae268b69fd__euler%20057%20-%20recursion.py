from fractions import Fraction

import sys
sys.setrecursionlimit(10000)

def squareRoot(expansions_count):
    if expansions_count == 1:
        return 2
    return 2 + Fraction(1, squareRoot(expansions_count-1))

"""
for i in range(1, 10):
    square2 = 1 + Fraction(1, squareRoot(i))
    print (repr(square2), float(square2))
"""

result = 0
for i in range(1, 1001):
    square2 = 1 + Fraction(1, squareRoot(i))
    if len(str(square2.numerator)) > len(str(square2.denominator)):
        result += 1

# answer is 153 (because of very tail recursion calculation tooks pretty long time)
print ("In 1000 expansions, %d fractions contain a numerator with more digits than denominator" % result)
