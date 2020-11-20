# Fettet, Louis
# Insertion Sort
# 12/15/12

def insertionSort(l):
    """
    Returns "s" as a sorted list in worst case O(n**2) runtime.
    """
    for i in range(len(l)):
        j = i
        while j > 0 and l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
            j -= 1
    return l
