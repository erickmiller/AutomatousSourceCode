# mergeSort.py

def mergeSort(lst):
    
    if len(lst) == 1:
        return lst
    
    else:
        mid = len(lst)//2
        left = mergesort(lst[:mid])
        right = mergesort(lst[mid:])
        
        sorted_ = []
        a = 0
        b = 0
        # a and b are index values for left and right, respectively
        # a and b are always the first (or next one to be considered) position of their lists
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                sorted_.append(left[a])
                a += 1
            else:
                sorted_.append(right[b])
                b += 1
        if a == len(left):
            sorted_.extend(right[b:])
        else:
            sorted_.extend(left[a:])
        return sorted_

