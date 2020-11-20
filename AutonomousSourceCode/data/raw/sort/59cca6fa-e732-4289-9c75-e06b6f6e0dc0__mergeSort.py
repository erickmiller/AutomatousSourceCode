def merge(l1, l2):
    """
    recursively merges two sorted lists.
    
    l1, l2: SORTED lists.
    
    returns one sorted list.
    """

    if l1 == []:
        return l2
    
    elif l2 == []:
        return l1
    
    elif l1[0] < l2[0]:
        return [l1[0]] + merge(l1[1: ], l2)
    
    return [l2[0]] + merge(l1, l2[1: ])

def mergeSort(L):
    """
    recursively divides the list into two halves.
    calls merge function on the sorted halves after
    reaching the base case.

    returns the sorted list.
    """
    l = len(L)
    if l < 2:
        return L
    
    left = mergeSort(L[ :l/2])
    right = mergeSort(L[l/2: ])
    
    return merge(left, right)


length = int(input('Number of elements: '))
L = []
for i in range(length):
    n = int(input('Element ' + str(i + 1) + ': '))
    L.append(n)

L = mergeSort(L)
print '\nSorting...\n'
print L
print '\nSorted!\n'
