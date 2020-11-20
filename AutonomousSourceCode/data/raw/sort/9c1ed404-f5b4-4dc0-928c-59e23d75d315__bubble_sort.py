#  Sorting a list by comparing it's elements two by two and putting the biggest in the end

def sort_two_by_two(ul):

    for index in range(len(ul)):
        try:
            el1 = ul[index]
            el2 = ul[index + 1]
            if el1 > el2:
                ul[index] = el2
                ul[index +1] = el1
        except IndexError:
            return ul


def bubble(ul):

    sorted_list = ul
    copyed_list = []
    while copyed_list != sorted_list:
        copyed_list = sorted_list[:]
        sorted_list = sort_two_by_two(sorted_list)
    return sorted_list
