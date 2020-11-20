'''
Created on Nov 1, 2011

@author: mark
'''
import copy

def sorted_list (t):
    r = copy.copy(t)
    r.sort()
    return r

if __name__ == '__main__':
    a = [30, 20000, 300, 40]
    b = ['crunchy frog', 'ram bladder', 'lark vomit']
    print sorted_list(a)
    print sorted_list(b)
    print a
    print b