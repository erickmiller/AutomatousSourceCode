__author__ = 'TeaEra'


def insertion_sort(arr):
    size = len(arr)
    if size <= 1:
        return arr
    sliced_arr = arr[1:]
    sorted_sliced_arr = insertion_sort(sliced_arr)
    for i in range(len(sorted_sliced_arr)):
        if arr[0] < sorted_sliced_arr[i]:
            return sorted_sliced_arr[:i] + [arr[0]] + sorted_sliced_arr[i:]
    return sorted_sliced_arr + [arr[0]]

if __name__ == "__main__":
    #
    print("---")
    print(insertion_sort([]))
    #
    print("---")
    print(insertion_sort(["abc"]))
    #
    print("---")
    print(insertion_sort([9, 1, 3, 7, 4, 2, 8, 5, 0]))