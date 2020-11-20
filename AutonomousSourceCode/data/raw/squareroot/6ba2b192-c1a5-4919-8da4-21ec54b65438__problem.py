# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:02:08 2014

@author: ventilator
"""

import profile
from fractions import Fraction
        
def create_continued_fraction(layers):
    if layers == 0:
        half = Fraction(1,2)
        half = 2
        return half
    else:       
        next_layer = Fraction(2 + Fraction(1, create_continued_fraction(layers - 1)))        
        return next_layer


def square_root_two(layers):
    # this intermediate layer is to fix for leading 1 instead of 2
    return Fraction(1 + Fraction(1, create_continued_fraction(layers)))
    
    


def solve_problem():  

    max_range = 1000
    count = 0

    for i in range(max_range):
        current_square_root = square_root_two(i)
        numerator = len(str(current_square_root.numerator))
        denominator = len(str(current_square_root.denominator))
        if numerator > denominator:
            count += 1
            #print(current_square_root)
        if i % 10 == 0: print("progress: " + str(i/max_range*100))    
        
    print("Condition fulfilled by:")    
    print(count)    
    
    return 0
    
solve_problem()    
# profile.run('solve_problem()')   