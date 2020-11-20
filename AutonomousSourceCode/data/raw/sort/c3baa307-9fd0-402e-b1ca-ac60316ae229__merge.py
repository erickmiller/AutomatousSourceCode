def sort(values):
    return split(values)


def merge(left, right):
    sorted_list = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        elif len(left) > 0:
            sorted_list.append(left.pop(0))
        elif len(right) > 0:
            sorted_list.append(right.pop(0))

    return sorted_list


def split(values):
    if len(values) is 1:
        return values

    split_value = len(values)/2
    x = split(values[:split_value])
    y = split(values[split_value:])

    return merge(x, y)
