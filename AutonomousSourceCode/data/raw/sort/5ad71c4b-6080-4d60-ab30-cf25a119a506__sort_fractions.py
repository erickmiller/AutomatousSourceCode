def sort_fractions(fractions):
    list_of_values = []
    sorted_list_of_tuples = []
    temp_dict = {}
    for item in fractions:
        list_of_values.append(item[0] / item[1])
        temp_dict[item[0] / item[1]] = item
    list_of_values.sort()
    for item in list_of_values:
        sorted_list_of_tuples.append(temp_dict[item])
    return sorted_list_of_tuples
print(sort_fractions([(1, 2), (1, 3), (3, 4)]))
