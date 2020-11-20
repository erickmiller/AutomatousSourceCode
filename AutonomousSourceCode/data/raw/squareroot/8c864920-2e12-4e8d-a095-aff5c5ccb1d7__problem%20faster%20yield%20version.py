# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:02:08 2014

@author: ventilator
"""

import profile
from fractions import Fraction

lut_square_root = []
        
def create_continued_fraction(layers):
    if layers == 0:
        half = Fraction(1,2)
        half = 2
        return half
    else:       
        current_layer = Fraction(2 + Fraction(1, create_continued_fraction(0))) 
        lut_square_root.append(current_layer)
        
        next_layer = Fraction(2 + Fraction(1, create_continued_fraction(layers - 1)))                
        return next_layer

def square_root_two(layers):
    # this intermediate layer is to fix for leading 1 instead of 2
    return Fraction(1 + Fraction(1, create_continued_fraction(layers)))


def yield_square_root(layers):
    # manual generate the first two items
    yield Fraction (3, 2)
    yield Fraction (7, 5)
    
    # iterate all the others
    current_depth = 2
    half = Fraction(1,2)
    
    lowest_layer = Fraction(2 + half)
    current_root = Fraction(1, lowest_layer) + 2
    
    while current_depth < layers:        
        yield Fraction(1, current_root) + 1
        current_depth += 1
        current_root = Fraction(1, current_root) + 2


def check_if_numerator_larger_denominator(number_as_fraction):
        numerator = len(str(number_as_fraction.numerator))
        denominator = len(str(number_as_fraction.denominator))
        return numerator > denominator   

def solve_problem():  

    # check if yield function is same as recursive function   
     
#    for i,iterative in enumerate(yield_square_root(20)):        
#        recursive = square_root_two(i)
#        print(i, iterative == recursive, iterative,  recursive)        
      
        
    max_range = 1000
    count = 0

    for i, square_root in enumerate(yield_square_root(max_range)):
        if check_if_numerator_larger_denominator(square_root):
            count += 1
            # print(i+1)
        # if i % 10 == 0: print("progress: " + str(i/max_range*100))    
        
    print("Condition fullfilled by:")    
    print(count)    
    
    return 0
    
#solve_problem()    
profile.run('solve_problem()')   