import math
import random

l = []
for i in range(0,2 ** 24):
    l.append(i)

random.shuffle(l)

print "sort start"

def sort(l):
    if len(l) == 1 or len(l) == 0:
        return l
    pivot = random.choice(l)
    less = []
    more = []
    for i in l:
        if i < pivot:
            less.append(i)
        else:
            more.append(i)
    print abs(len(more) - len(less))
    return sort(less) + sort(more)

def abs(n):
    return max(n, -n)

def isSorted(l):
    prev = l[0];
    for i in l:
        if i < prev:
            return False
        else:
            prev = i
    return True

l2 = sort(l)
print "sort done"

print isSorted(l2)
