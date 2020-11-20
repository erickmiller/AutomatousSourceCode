def selection_sort(list):
    sorted_list = list[:]

    for i in range(0, len(sorted_list)):
        pos_min = i
        for j in range(i, len(sorted_list)):
            if sorted_list[pos_min] > sorted_list[j]:
                pos_min = j

        temp = sorted_list[i]
        sorted_list[i] = sorted_list[pos_min]
        sorted_list[pos_min] = temp

    return sorted_list