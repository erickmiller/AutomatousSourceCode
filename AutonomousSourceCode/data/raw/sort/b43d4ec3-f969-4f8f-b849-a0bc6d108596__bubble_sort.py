def bubble_sort(arr):
    size = len(arr)
    if size < 2:
        return
    
    scanLimit = size - 1
    sorted = False
    
    while not sorted:    
        sorted = True
        i = 0
        
        while i < scanLimit:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
            i += 1
        
        scanLimit -= 1

    return