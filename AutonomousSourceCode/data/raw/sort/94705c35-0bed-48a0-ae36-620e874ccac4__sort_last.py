#!/usr/bin/python

def sort_last(x): 
    return sorted(x, key=lambda x:x[-1])
 
print sort_last([[1, 3], [3, 2], [2, 1]]) 
print sort_last([[2, 3], [1, 2], [3, 1]]) 
print sort_last([[1, 7], [1, 3], [3, 4, 5], [2, 2]])