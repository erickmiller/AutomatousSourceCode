#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-17
根据对象的属性将对象列表排序
@author: CaiKnife
'''

#Python 2.3
def sort_by_attr(seq, attr):
    intermed = [(getattr(x, attr), i, x) for i, x in enumerate(seq)]
    intermed.sort()
    return [x[-1] for x in intermed]

def sort_by_attr_inplace(lst, attr):
    lst[:] = sort_by_attr(lst, attr)
    

#Python 2.4+
import operator
def sort_by_attr_new(seq, attr):
    return sorted(sq, key=operator.attrgetter(attr))

def sort_by_attr_inplace_new(lst, attr):
    lst.sort(key=operator.attrgetter(attr))
    
