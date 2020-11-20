# nlogn, divide and conquer
# recursive

def merge_sort(int_array):
    # base case
    if len(int_array) == 0:
        return None
    elif len(int_array) == 1:
        return int_array

    # recursive step
    else:
        l = len(int_array)/2
        first_half = int_array[:l]
        second_half = int_array[l:]
        sorted_first_half = merge_sort(first_half)
        sorted_second_half = merge_sort(second_half)
        return merge_sorted_lists(sorted_first_half, sorted_second_half)

def merge_sorted_lists(first, second):
    sorted_complete_list = []

    while first or second:
        if first and second:
            if first[0] <= second[0]:
                sorted_complete_list.append(first[0])
                first = first[1:]
            else:
                sorted_complete_list.append(second[0])
                second = second[1:]
        elif first:
            sorted_complete_list.extend(first)
            break
        elif second:
            sorted_complete_list.extend(second)
            break

    return sorted_complete_list

if __name__ == "__main__":
    # from pudb import set_trace; set_trace()
    eight_element_list = [8, 0, 12, 2, 5, 7, 3, 10]
    print eight_element_list
    print merge_sort(eight_element_list)
    print

    odd_number_element_list = [-10, 5, 2, 7, 6, 4.4, 3.75]
    print odd_number_element_list
    print merge_sort(odd_number_element_list)
    print

    list_w_dups = [8, 8, 3, 3, 3, 4, 4, 0]
    print list_w_dups
    print merge_sort(list_w_dups)
    print

    sorted_list = [1, 1, 3, 3, 6, 6, 9, 9, 1000, 1000, 5000, 5000, 100000000]
    print sorted_list
    print merge_sort(sorted_list)
    print

    rev_sorted_list = [10, 9, 8, 7, 6, 0, -5, -10]
    print rev_sorted_list
    print merge_sort(rev_sorted_list)
    print
