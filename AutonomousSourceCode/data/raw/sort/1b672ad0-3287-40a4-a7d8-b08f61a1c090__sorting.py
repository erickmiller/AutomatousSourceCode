def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst)/2
    lst_a = merge_sort(lst[0:mid])
    lst_b = merge_sort(lst[mid:])

    sorted_list = []

    while len(lst_a) > 0 and len(lst_b) > 0:
        if lst_a[0] > lst_b[0]:
            sorted_list.append(lst_b.pop(0))
        else:
            sorted_list.append(lst_a.pop(0))

    sorted_list.extend(lst_a)
    sorted_list.extend(lst_b)

    return sorted_list


def bubble_sort(lst):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                sorted = False


def insertion_sort(lst):
    for i in range(1, len(lst)):

        left_item_index = i - 1
        current_item = lst[i]

        while left_item_index >= 0 and current_item < lst[left_item_index]:
            lst[left_item_index + 1] = lst[left_item_index]
            lst[left_item_index] = current_item
            left_item_index = left_item_index - 1


def main():
    pass

if __name__ == "__main__":
    main()