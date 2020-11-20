'''
Square Root Convergents
'''
from fractions import Fraction

def frac_iter(n, v=Fraction(1,2)):
    '''Yield expression for n expansions'''
    while n > 0:
        yield Fraction(1,1) + v
        v = Fraction(1, Fraction(2,1) + v)
        n -= 1
    return

if __name__ == '__main__':
    print sum(1 if len(str(f.numerator)) > len(str(f.denominator)) else 0\
            for f in frac_iter(1000))
