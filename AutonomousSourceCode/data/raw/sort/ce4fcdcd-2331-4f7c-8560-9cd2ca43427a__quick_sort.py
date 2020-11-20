f = open ('QuickSort.txt', 'r')
ar = [int(i) for i in f];
f.close()

def median(a):
    return sorted(a)[1]

def quick_sort(a):
    return _quick_sort(a, 0, len(a))

def _quick_sort(a, l, r):
    c = 0
    if l < r:
        q, c = _partition(a, l, r)
        c += _quick_sort(a, l, q-1)
        c += _quick_sort(a, q, r)
    return c

def _partition(a, l, r):
    p = median([a[l], a[l+(r-l-1)/2], a[r-1]])
    if a[l] == p:
        p_i = l
    elif a[l+(r-l-1)/2] == p:
        p_i = l+(r-l-1)/2
    else:
        p_i = r-1
    a[l], a[p_i] = a[p_i], a[l]
    i = l + 1
    c = 0
    for j in xrange(l+1, r):
        c += 1
        if a[j] < p:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]
    return i, c
#ar = [7, 5, 1, 4, 8, 3, 10, 2, 6, 9]
count = quick_sort(ar)
print count
