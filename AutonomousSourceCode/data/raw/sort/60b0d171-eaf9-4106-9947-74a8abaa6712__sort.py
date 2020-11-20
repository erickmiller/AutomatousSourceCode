def quickSort (arr):
    """ Quicksort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if not arr:
        return []
    pivots  = []
    lesser  = []
    greater = []
    for x in arr:
        if x==arr[0]:
           pivots.append(x)
        elif x>arr[0]:
            greater.append(x)
        else:
            lesser.append(x)
    return quickSort(lesser) + pivots + quickSort(greater)

test_array = [1,4,5,7,8,9,90,3,2,3,4]
sorted_array = quickSort (test_array)
print "unsorted:",test_array,"Sorted:",sorted_array
