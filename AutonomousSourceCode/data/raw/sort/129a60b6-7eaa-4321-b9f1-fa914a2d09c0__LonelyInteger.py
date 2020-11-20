"""
David Schonberger
Hackerrank.com
Search - Lonely Integer
1/13/2015
"""

def mergeSort(lst, c):
    if len(lst) < 2:
        return lst
    m = len(lst) / 2
    return merge(mergeSort(lst[:m], c), mergeSort(lst[m:], c), c)

def merge(l, r, c):
    res = []
    while(l and r):
        if(l[0] <= r[0]):
            s = l
        else:
            s = r
        res.append(s.pop(0))
        if(s == r and not s == l):
            c[0] += len(l)
            
    res.extend(l if l else r)
    return res


N = input()
ar = raw_input()
ar = ar.split(' ')
ar = [int(t) for t in ar]

if(len(ar) == 1):
    print ar[0]
else:
    count = [0]
    ar_sorted = mergeSort(ar, count)
    found = False    
    i = 0
    while(not found and i < len(ar_sorted) - 1):
        if(ar_sorted[i] != ar_sorted[i+1]):
            found = True
            res = ar_sorted[i]
        i += 2
    if(i == len(ar_sorted) - 1):
        res = ar_sorted[i]
    print res
