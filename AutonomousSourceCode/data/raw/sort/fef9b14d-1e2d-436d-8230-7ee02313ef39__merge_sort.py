unsorted_lists = [
    [3, 4, 6, 5],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 5, 6, 7, 9, 0],
    [-1, -5, -3, -4],
    [4, 3, 2, 1, 9, 8, 7, 6, 5],
]


def merge_sort(unsorted_list):
    # print("Splitting: {0}".format(unsorted_list))
    if len(unsorted_list) <= 1:
        return unsorted_list
    mid = len(unsorted_list) // 2
    left_half = merge_sort(unsorted_list[:mid])
    right_half = merge_sort(unsorted_list[mid:])
    # print("Left Half: {0}".format(left_half))
    # print("Right Half:  {0}".format(right_half))

    # Merge
    sorted_list = []
    i, k = 0, 0
    while i < len(left_half) and k < len(right_half):
        if left_half[i] < right_half[k]:
            sorted_list.append(left_half[i])
            i += 1
        else:
            sorted_list.append(right_half[k])
            k += 1

    sorted_list.extend(left_half[i:])
    sorted_list.extend(right_half[k:])

    return sorted_list


if __name__ == '__main__':

    # print(merge_sort(unsorted_lists[0]))
    for ulist in unsorted_lists:
        print(merge_sort(ulist))
