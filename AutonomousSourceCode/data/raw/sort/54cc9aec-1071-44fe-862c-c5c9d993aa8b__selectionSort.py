def swap(a,i,j):
    old = a[i]
    a[i] = a[j]
    a[j] = old
    return a
def selectionSort(a):
    l = len(a)
    for i in range(l):
        m = i
        for j in range(i+1,l):
            if a[j]<a[m]:
                m = j
        swap(a,m,i)
    #print "sorted?: "+str(a==sorted(a))
    return a
print selectionSort([1,3,6,4,123,756,13,79,23467,1,43,67])

        
