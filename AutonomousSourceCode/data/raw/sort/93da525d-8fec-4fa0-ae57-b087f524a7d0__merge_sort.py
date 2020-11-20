# Merge sort algorithm: a sorting method that uses divide and
# conquer algo recursively to produce a sorted list in
# ascending order -- Vivi.

from random import randrange

def merge(lst1, lst2):
    """
    input 2 unsorted lists
    output a sorted list in ascending order
    """
    
    idx = 0 # idx for index of list 1
    jdx = 0 # jdx for index of list 2
    
    # initialize empty list to store sorted answer
    sorted_lst = []
    
    # loop ends whever one of the index 
    # reache the end of the list
    while idx != len(lst1) and jdx != len(lst2):
        
        # compare the element of corresponding indices
        # of both list and append the smaller one 
        # to the answer
        if lst1[idx] < lst2[jdx]:
            sorted_lst.append(lst1[idx])
            idx += 1
        else:
            sorted_lst.append(lst2[jdx])
            jdx += 1
    
    # append remaining elements at the end of 
    # the sorted list if any is left.
    sorted_lst.extend(lst1[idx:])
    sorted_lst.extend(lst2[jdx:])
    
    return sorted_lst

def merge_sort(lst):
    """
    a recursive method to sort a list into ascending order
    """
    
    # base case
    if len(lst) < 2:
        return lst
    # recursive case
    else:
        half1 = lst[:len(lst)//2]
        half2 = lst[len(lst)//2:]
        
        sorted_1 = merge_sort(half1)
        sorted_2 = merge_sort(half2)
        
        return merge(sorted_1, sorted_2)
    


def merge_sort_test():
    """
    function to test merge_sort with random numbers
    """
    failed = 0
    for trial in range(100):
        length = randrange(1, 10)
        idx = 0
        lst = []
        for item in range(length):
            lst.append(randrange(1, 999))
            
        
        sorted_lst = merge_sort(lst)
        if sorted_lst != sorted(lst):
            failed += 1
    
    if failed > 0:
        print "test failed for ", str(failed), " of cases."
    else:
        print "test passed!! :)"
        
merge_sort_test()