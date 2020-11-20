#!/usr/bin/python 
from math import sqrt 
def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5)**2 == integer:
        return True 
    else:
        return False 

if __name__ == '__main__':
    import sys 
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        res = sum([ 1 for i in range(a,b+1) if is_square(i) ])
        print(res)
