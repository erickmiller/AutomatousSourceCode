def bubble_sort(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
    if array == sorted(array):
        return array
    else:
        return bubble_sort(array)

bubble_sort([1, 2, 3, 4])
bubble_sort([1, 3, 2, 4, 6, 5])
