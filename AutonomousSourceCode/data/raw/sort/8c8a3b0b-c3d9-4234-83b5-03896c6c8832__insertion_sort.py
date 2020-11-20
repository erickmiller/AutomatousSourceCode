def insertion_sort(list):
    sorted_list = list[:]

    for index in range(0, len(list)):
        current_value = sorted_list[index]
        position = index

        while position > 0 and current_value < sorted_list[position - 1]:
            sorted_list[position] = sorted_list[position - 1]
            position -= 1

        sorted_list[position] = current_value

    return sorted_list