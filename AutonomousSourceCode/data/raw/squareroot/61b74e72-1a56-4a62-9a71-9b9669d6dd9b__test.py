__author__ = 'VadymT'
__date__ = '19th Apr 2015'
import math

def test_square_root(s1,s2):
    for i in range(s1,s2):
        a = i ** 0.5
        b = math.sqrt(i)
        if (a).is_integer():
            print ("%1.1f\t %1.1f \t\t\t%1.1f \t\t\t%1.1f" % (i, a, b, a - b ))
        else:
            print ("%1.1f\t %13.11f\t%13.11f\t%16.13e" % (i, a, b, a - b))
    return True

test_square_root(1, 10)
