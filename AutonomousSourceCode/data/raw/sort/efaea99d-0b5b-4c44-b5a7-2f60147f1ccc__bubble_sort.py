def bubble_sort(list):
    sorted_list = list[:]

    for i in range(0, len(sorted_list)):
        for j in range(0, len(sorted_list) - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp

    return sorted_list