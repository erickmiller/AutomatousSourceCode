#!/usr/bin/env python

def square_root(a, x):
    while True:
        y = (x + a/x) / 2      
        if abs(y-x) < 0.0000001:
            return x
        x = y    
        
if __name__ == '__main__':
    print square_root(4.0, 3.0)
