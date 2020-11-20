#!/usr/bin/env python

def is_sorted(collection):
    a = [ c for c in collection]
    a.sort()
    return a == collection
    

if __name__ == '__main__':
    print is_sorted([1, 2, 2])
    print is_sorted(['b', 'a'])