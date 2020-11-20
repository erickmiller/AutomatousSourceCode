def swap(a,i,j):
    a[i],a[j]=a[j],a[i]
  #  old = a[i]
  #  a[i] = a[j]
  #  a[j] = old

def insertionSort(a):
    l = len(a)
    for i in range(1,l):
        p = i
        while a[p-1]>a[p] and p > 0:
            swap(a,p,p-1)
            p -= 1
    return a

a = insertionSort([4,78,123,87,132,5,7,1,3,8,2,8,4,1,248])
print a
print "Sorted?: "+str(a==sorted(a))
