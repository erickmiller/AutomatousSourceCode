def partition(a, l, r):
    p = a[l]
    i = l + 1
    for j in xrange(l + 1, r):
        if a[j] > p: continue
        a[j], a[i] = a[i], a[j]
        i += 1
    a[l], a[i - 1] = a[i - 1], a[l]
    return i - 1

def choosePivot(a, l, r):
    #return r - 1
    if 2 == (l - r): return l
    first = a[l]
    final = a[r - 1]
    if 0 == ((r - l) % 2): i = ((r - l) / 2) - 1
    else: i = (r - l) / 2
    mid = a[l + i]
    if (first < mid < final) or (final < mid < first): return l + i
    elif (mid < first < final) or (final < first < mid): return l
    else: return r - 1

def qSort(a, l, r):
    if r - l <= 1: return 0
    p = choosePivot(a, l, r)
    a[l], a[p] = a[p], a[l]
    tot = r - l - 1
    i = partition(a, l, r)
    tot += qSort(a, l, i)
    tot += qSort(a, i + 1, r)
    return tot

if "__main__" == __name__:
    a = []
    with open('QuickSort.txt', 'r') as f:
        for line in f:
            a.append(int(line))
    tot = qSort(a, 0, len(a))
    sorted = True
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            sorted = False
            break
    print 'Comparisons: %d' % tot
    if sorted: print 'Sorted'
    else: print 'Incorrectly sorted!'