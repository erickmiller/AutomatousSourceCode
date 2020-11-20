# http://projecteuler.net/problem=64
import math

def getRootSequence(r):
    """ See problem statement for details """
    a = -1 * math.floor(math.sqrt(r))
    b = 1
    
    sequence = []
    for i in range(500):
        d, r, a, b = helper(r, a, b)
        sequence.append(d) 

    return sequence

def helper(r, a, b):
    """ 
    Finds the next integer answer and returns the new fraction in terms
    of r, a, and b:   b / (r + a)
    """
    c = r - (a * a)
    d = int(math.floor(b * (math.sqrt(r) - a) / c))

    newA = (-1 * a) - (c * d / b)
    newB = c / b

    return d, r, newA, newB

def getPeriod(sequence):
    """ Returns the period of the repeating sequence """
    for period in range(1, len(sequence)):
        sequences = [tuple(sequence[j*period :j*period + period]) for j in range(len(sequence) / period)]
        if len(set(sequences)) == 1:
            return period

def isPerfectSquare(n):
    root = math.sqrt(n)
    return True if int(root + 0.5) ** 2 == n else False
        

total = 0
roots = [r for r in range(2, 10001) if not isPerfectSquare(r)]
periods = [getPeriod(getRootSequence(root)) for root in roots]
print len([period for period in periods if period % 2 == 1])
