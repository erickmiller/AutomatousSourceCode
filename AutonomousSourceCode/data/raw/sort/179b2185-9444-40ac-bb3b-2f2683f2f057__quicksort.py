def quickSort (arr):
    """ Quicksort a list
 
    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if not arr:
        return []
 
    pivots = [x for x in arr if x == arr[0]]
    lesser = quickSort([x for x in arr if x < arr[0]])
    greater = quickSort([x for x in arr if x > arr[0]])
 
    return lesser  + pivots + greater
 
test_array = [1 ,4,5,7,8,9,90,3,2,3,4]
sorted_array = quickSort (test_array)
print sorted_array
