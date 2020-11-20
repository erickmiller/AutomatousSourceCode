__author__ = 'Aristide'

def main():
    list_to_sort = raw_input("Enter the numbers to sort, e.g: 53784298 : ")
    print sort(map(lambda char: int(char)), list(list_to_sort))


def sort(unsorted_list):
    """
    sort splits any list with more than one element in two parts, calls itself on the sublists,
    and calls merge with the returned sorted lists. When the parameter is an empty list or a
    single element list, sort just returns the list as the output.

    Doctests:
    Test empty list
        >>> sort([])
        []

    Test single element list
        >>> sort([3])
        [3]

    Test all even length sublists list
        >>> sort([9,3,6,7,5,4,3,2])
        [2, 3, 3, 4, 5, 6, 7, 9]

    Test odd length list
        >>> sort([9,3,6,8,7,5,4,3,2])
        [2, 3, 3, 4, 5, 6, 7, 8, 9]

    """
    output = []

    if len(unsorted_list) <= 1:
        output = unsorted_list
    else:
        # For odd length lists, Integer division allows a left sublist that is one element smaller than the right
        # sublist, for free :)
        left_sorted_list = sort(unsorted_list[0:(len(unsorted_list)/2)])
        right_sorted_list = sort(unsorted_list[(len(unsorted_list)/2):])

        output = merge(left_sorted_list, right_sorted_list)

    return output


def merge(left_sorted_list, right_sorted_list):
    """
    merge traverses each sorted list comparing the front elements. The smaller of the two is the next element in the
    sorted merged list
    """
    merged_sorted_list = [None] * (len(left_sorted_list) + len(right_sorted_list))

    iLeft = 0
    iRight= 0

    iMerged = 0

    while iMerged < len(merged_sorted_list):
        if iLeft == len(left_sorted_list):
            merged_sorted_list[iMerged:] = right_sorted_list[iRight:]
            iMerged = len(merged_sorted_list)
        elif iRight == len(right_sorted_list):
            merged_sorted_list[iMerged:] = left_sorted_list[iLeft:]
            iMerged = len(merged_sorted_list)
        elif left_sorted_list[iLeft] < right_sorted_list[iRight]:
            merged_sorted_list[iMerged] = left_sorted_list[iLeft]
            iLeft += 1
            iMerged += 1
        else:
            merged_sorted_list[iMerged] = right_sorted_list[iRight]
            iRight +=1
            iMerged += 1

    return merged_sorted_list


if __name__ == "__main__":
    # main()
    import doctest
    doctest.testmod(verbose=True)
