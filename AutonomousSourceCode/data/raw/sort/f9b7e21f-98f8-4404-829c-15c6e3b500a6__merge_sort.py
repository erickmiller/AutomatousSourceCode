def merge_sort(unsorted):
    """ Base case """
    if len(unsorted) <= 1:
        return unsorted

    """ Split array into two halves """
    mid = len(unsorted) // 2
    left_half = merge_sort(unsorted[:mid])
    right_half = merge_sort(unsorted[mid:])

    return merge(left_half, right_half)

def merge(left_half, right_half):
    """ Compare halves and merge into sorted list """
    sorted_list = []

    while len(left_half) > 0 and len(right_half) > 0:
        if left_half[0] < right_half[0]:
            sorted_list.append(left_half.pop(0))
        else:
            sorted_list.append(right_half.pop(0))

    if len(left_half) > 0:
        sorted_list.extend(left_half)

    if len(right_half) > 0:
        sorted_list.extend(right_half)

    return sorted_list

unsorted = [98, 35, 28, 44, 10, 6, 110]
print merge_sort(unsorted)
