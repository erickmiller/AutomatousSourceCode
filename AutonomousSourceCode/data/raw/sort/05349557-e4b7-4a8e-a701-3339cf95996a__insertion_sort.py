def sort(arr):
    for idx in range(1, len(arr)):
        insert(arr, idx, arr[idx])
    return arr

def insert(arr, pos, val):
    i = pos - 1
    while i >= 0 and arr[i] > val:
        arr[i + 1] = arr[i]
        i = i -1
    arr[i + 1] = val

if __name__ == '__main__':
    test_set = [7, 6, 2, 5, 4, 6, 1, 3, 10, 50, 3]
    print 'Sorting: {0}'.format(test_set)
    sorted_set = sort(test_set)
    print 'Sorted: {0}'.format(sorted_set)