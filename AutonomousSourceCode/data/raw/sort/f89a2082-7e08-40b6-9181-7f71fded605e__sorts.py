import random
from collections import deque

def quick_sort(l):
    if len(l) < 2:
        return l
    piv = random.randint(0, len(l)-1)
    smaller = []
    larger = []
    
    # left slice
    for item in l[0:piv]:
        if item > l[piv]:
            larger.append(item)
        else:
            smaller.append(item)
    # right slice
    for item in l[piv+1:]:
        if item > l[piv]:
            larger.append(item)
        else:
            smaller.append(item)

    sorted_smlr = quick_sort(smaller)
    sorted_lrgr = quick_sort(larger)
    return sorted_smlr + [l[piv]] + sorted_lrgr


def merge_sort(l):
    if len(l) < 2:
        return l
    l1 = l[0:len(l)/2]
    l2 = l[len(l)/2:]
    print "l1:%s" % l1
    print "l2:%s" % l2
    
    sorted_l1 = deque(merge_sort(l1))
    sorted_l2 = deque(merge_sort(l2))
    sorted_l = []

    while len(sorted_l1) > 0 and len(sorted_l2) > 0:
        if sorted_l1[0] > sorted_l2[0]:
            sorted_l.append(sorted_l2.popleft())
        else:
            sorted_l.append(sorted_l1.popleft())
        
    if len(sorted_l1) > 0:
        sorted_l += list(sorted_l1)

    if len(sorted_l2) > 0:
        sorted_l += list(sorted_l2)
    
    return sorted_l


if __name__ == '__main__':
    import numpy as np
    import datetime

#    sizes = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000, 20000000, 50000000, 100000000]
#    sizes = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
    sizes = [20]

    for siz in sizes:
        
        l = np.random.randint(siz, size=siz)
        print "source: %s" % l

        t0 = datetime.datetime.now()

#        result = quick_sort(l)
        result = merge_sort(l)

        dt = datetime.datetime.now() - t0

        print "result: %s" % result    
        print "%d\t%d days %d seconds %d microsecondsecs" % (siz, dt.days, dt.seconds, dt.microseconds)


