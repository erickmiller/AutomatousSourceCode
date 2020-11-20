from math import *
from decimal import Decimal

def euclidian_distance(a,b ):
    ''' a and b are vector '''
    if len(a) != len(b):
        raise ValueError("a and b has not the same size ")

    return  sqrt(sum(pow(x-y,2) for x, y in zip(a, b)))

#===============================================================

def manathan_distance(a,b):
    ''' a and b are vector '''
    if len(a) != len(b):
        raise ValueError("a and b has not the same size ")

    return sum(abs(x-y) for x,y in zip(a,b))

#===============================================================

def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)

def minkowski_distance(x,y,p_value):
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)

#===============================================================
def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)
#===============================================================
