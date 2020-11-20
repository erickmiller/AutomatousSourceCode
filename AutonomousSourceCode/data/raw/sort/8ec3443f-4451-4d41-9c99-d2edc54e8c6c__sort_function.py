def insertion_sort(input_list):
    if type(input_list) != 'list':
        input_list = list(input_list)

    sorted_list = []

    sorted_list.append(input_list[0])

    for item in input_list[1:]:
     
        if item >= sorted_list[-1]:
            sorted_list.append(item)

        else:
            for i in range(len(sorted_list)):
                if item < sorted_list[i]:
                    sorted_list.insert(i, item)
                    i +=1
                    break

    return sorted_list

l = [4, 5, 6, 19, 11, 2, 3]

s = ['cat', 'dog', 'bunny', 'apple']

t = (1, 5, 3, 2)

print insertion_sort(l)
print insertion_sort(s)
print insertion_sort(t)