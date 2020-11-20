def bubble_sort(a):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a = a[:i-1] + a[i] + a[i-1] + a[i+1:]
                sorted = False
    return a

#RESULT: Merge sort is 276.263642 times faster than bubble sort.