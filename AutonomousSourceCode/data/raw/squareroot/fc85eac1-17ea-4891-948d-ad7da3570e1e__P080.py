#!/usr/bin/env python3

import decimal
import math
import sys

def is_square(number):
    root = int(round(math.sqrt(number)))
    return root ** 2 == number

def solve(N, P):
    decimal.getcontext().prec = P + 5
    return sum([sum(map(int, list(filter(lambda digit: digit != '.', list(str(decimal.Decimal(number).sqrt()))))[:P])) for number in range(1, N + 1) if not is_square(number)]) 

def main():
    print(solve(100, 100), file=sys.stderr)
    
    N = int(input())
    P = int(input())
    
    print(solve(N, P))

if __name__ == '__main__':
    main()
