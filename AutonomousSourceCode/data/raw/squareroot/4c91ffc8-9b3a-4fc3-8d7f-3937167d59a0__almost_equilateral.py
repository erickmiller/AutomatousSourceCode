#!/usr/bin/env python3

from math import sqrt

def isSquare(n):
    root = int(sqrt(n))
    if root**2==n or (root+1)**2==n:
        return True
    else:
        return False

def checkSeq1(n):
    true = []
    for i in range(2,n+1,2):
        if isSquare((i+2)*(3*i+2)):
            true.append(i)
    return true

def checkSeq2(n):
    true = []
    for i in range(2,n+1,2):
        if isSquare((i-2)*(3*i-2)):
            true.append(i)
    return true

def sequence(bound, starter_values):
    values = [i for i in starter_values]
    if values[-1]>=bound:
        return values
    while values[-1]<bound:
        values.append(15*values[-1]-15*values[-2]+values[-3])
    return values


