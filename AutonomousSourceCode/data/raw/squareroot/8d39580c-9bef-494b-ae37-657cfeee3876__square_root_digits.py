#!/usr/bin/env python3

def de_decimal(n):
    n=str(n)
    n="".join(n.split("."))
    return int(n)

def get_square_root(n,precision=100):
    """
    Used the square root by subtraction method by Frazer Jarvis
    """
    a=5*n
    b=5
    while len(str(b))<precision+2:
        if a>=b:
            a,b=a-b,b+10
        elif a<b:
            a,b=a*100,(b-5)*10+5
    return str(b)[:-2]

def main(upper=100, precision=100):
    a=0
    for i in range(1,upper+1):
        if not (i**0.5).is_integer():
            for j in get_square_root(i, precision):
                a+=int(j)
    return a
