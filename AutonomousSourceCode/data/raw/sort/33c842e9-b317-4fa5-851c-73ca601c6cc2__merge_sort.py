def merge(left, right):
    sorted_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list += left[i:]
    sorted_list += right[j:]
    return sorted_list


def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    mid = len(my_list) / 2
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])
    return merge(left, right)


l = [8, 100, 89, 1, 99, 20, 15, 46, 3, 2]
print merge_sort(l)
