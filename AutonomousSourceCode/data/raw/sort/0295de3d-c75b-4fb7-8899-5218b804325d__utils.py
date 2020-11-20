# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 15:56:48 2014

@author: SBader
"""

def compose(f1,f2):
    return lambda *args, **kwargs: f1(f2(*args,**kwargs))
    
def float_sorted_items(dictionary):
    try:
        sorted_keys=sorted(dictionary.keys(),key=float)
    except:
        sorted_keys=dictionary.keys()
    sorted_values=[dictionary[key] for key in sorted_keys]
    return zip(sorted_keys,sorted_values)
    
def float_sorted(lst):
    try:
        print lst
        print "let's sort"
        print sorted(lst,key=float)
        return sorted(lst,key=float)
    except:
        return lst
        
def flatten_lol(lst):
    return [x for sublst in lst for x in sublst]