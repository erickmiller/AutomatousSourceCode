# _*_ coding: utf-8 _*_

__author__ = 'TeaEra'


def quick_sort(arr):
    """
    en:
    QuickSort

    zh:
    快速排序
    """
    size = len(arr)
    if size <= 1:
        return arr
    pivot = arr[0]
    less_part = list()
    more_part = list()
    for i in range(1, size, 1):
        if arr[i] < pivot:
            less_part.append(arr[i])
        else:
            more_part.append(arr[i])
    sorted_less_part = quick_sort(less_part)
    sorted_more_part = quick_sort(more_part)
    return sorted_less_part + [pivot] + sorted_more_part

if __name__ == "__main__":
    #
    print("---")
    print(quick_sort([]))
    #
    print("---")
    print(quick_sort([9, 1, 3, 7, 4, 2, 8, 5, 0]))