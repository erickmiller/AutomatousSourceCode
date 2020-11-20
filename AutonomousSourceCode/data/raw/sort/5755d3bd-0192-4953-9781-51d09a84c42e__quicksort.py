def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    left = []
    right = []

    for ind in range(1, len(lst)):
        if lst[ind] <= lst[0]:
            left.append(lst[ind])
        else:
            right.append(lst[ind])

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)


    sorted_left.append(lst[0])
    sorted_left.extend(sorted_right)
    return sorted_left


lst = [3,2,5,6,7,4,1,8,9,10]
quick_sort(lst)
print(lst)
