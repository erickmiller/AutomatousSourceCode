import random


def random_quick_sort(list_to_sort):
    if len(list_to_sort) > 1:
        less = []
        equal = []
        greater = []
        pivot = list_to_sort[random.randrange(len(list_to_sort))]
        for x in list_to_sort:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return random_quick_sort(less) + equal + random_quick_sort(greater)
    else:
        return list_to_sort

array = [20, 3, 3, 19, 88, 7, 22, 7, 4, 2, 99]
sorted_array = random_quick_sort(array)
print(sorted_array)

pass
