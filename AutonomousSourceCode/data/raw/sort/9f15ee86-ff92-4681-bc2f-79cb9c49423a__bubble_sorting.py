__author__ = 'Vyacheslau Karachun'


def sort(array):
    is_sorted = False
    sorted_arr = array[:]
    while not is_sorted:
        difference_absent = True
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                sorted_arr[i] = array[i+1]
                sorted_arr[i+1] = array[i]
                difference_absent = False
        array = sorted_arr[:]
        if difference_absent:
            is_sorted = True
    return sorted_arr
