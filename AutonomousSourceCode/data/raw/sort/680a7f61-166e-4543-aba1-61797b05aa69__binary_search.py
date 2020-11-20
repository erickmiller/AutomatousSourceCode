__author__ = 'cwang'
from bisect import bisect_left


def binary_search(sorted_arr, target):
    pos = bisect_left(sorted_arr, target)
    return pos if pos < len(sorted_arr) and sorted_arr[pos] == target else -1

def my_binary_search(sorted_arr, target, lo, hi):
    if lo == hi:
        return lo
    mid = (lo + hi) // 2
    if target < sorted_arr[mid]:
        return my_binary_search(sorted_arr, target, lo, mid)
    elif target > sorted_arr[mid]:
        return my_binary_search(sorted_arr, target, mid + 1, hi)
    else:
        return mid

if __name__ == '__main__':
    arr = [1, 3, 5, 2, 4, 0]
    arr.sort()
    target = 1
    print(binary_search(arr, target))
    print(my_binary_search(arr, target, 0, len(arr)))
