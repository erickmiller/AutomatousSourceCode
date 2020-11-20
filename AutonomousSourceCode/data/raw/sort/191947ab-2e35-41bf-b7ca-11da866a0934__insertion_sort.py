
"""
Simple insertion sort
"""
import random

def swap_positions(index, li):
    while index > 0 and li[index] < li[index-1]:
        li[index-1], li[index] = li[index], li[index-1]
        index -= 1


def insertion_sort(dark_list):
    index_sorted_upto = 0
    for index, value in enumerate(dark_list):
        if value < dark_list[index_sorted_upto]:
            swap_positions(index, dark_list)
        index_sorted_upto = index
    return dark_list


def check_list_sorted(ar1):
    """
    checks if an array/list is sorted
    """
    return all(ar1[i] >= ar1[i-1] for i in range(1, len(ar1)))


def main():
    array_size = 1000
    numbers_range = 10000
    foo_ar = random.sample(range(0, numbers_range), array_size)
    
    print("before insertion_sort, is list sorted: {0}".format(check_list_sorted(foo_ar)))
    foo_ar = insertion_sort(foo_ar)
    print("after insertion_sort, is list sorted: {0}".format(check_list_sorted(foo_ar)))

    
if __name__ == '__main__':
	main()