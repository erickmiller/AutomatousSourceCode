# https://projecteuler.net/problem=52
# status = AC
# ans = 142857

import sys

def alphaSort(s):
    l = list(set(sorted(s)))
    return ''.join(sorted(l))

def isPermute(x):
    
    num = set()

    num.add(alphaSort(str(x)))

    if(     alphaSort(str(2*x)) in num 
            and alphaSort(str(3*x)) in num
            and alphaSort(str(4*x)) in num
            and alphaSort(str(5*x)) in num
            and alphaSort(str(6*x)) in num):
        return True
    else:
        return False

def solve():
    
    i = 1
    while True:
        if isPermute(i):
            return i
        i = i + 1

print solve()
