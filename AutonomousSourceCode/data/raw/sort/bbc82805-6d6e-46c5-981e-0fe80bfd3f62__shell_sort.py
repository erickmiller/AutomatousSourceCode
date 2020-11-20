# most stupid sort ever
def shell_sort(_list, step):
    sorted_list = _list[:]

    def sort_sublist(l, start, gap):
        for index in range(start, len(l), gap):
            current_value = l[index]
            position = index

            while position >= gap and current_value < l[position - gap]:
                l[position] = l[position - gap]
                position -= gap

            l[position] = current_value

    for i in range(0, step):
        sort_sublist(sorted_list, i, step)

    sorted_list = insertion_sort(sorted_list) 

    return sorted_list