import random

def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        pivot = len(array) / 2
        left_sorted = merge_sort(array[:pivot])
        right_sorted = merge_sort(array[pivot:])
        return merge(left_sorted, right_sorted)

def merge(array1, array2):
    merged = []
    while len(array1) > 0 and len(array2) > 0:
        merged.append(pop_smaller_head(array1, array2))
    remaining = array1 if len(array1) > 0 else array2
    return merged + remaining

def pop_smaller_head(array1, array2):
    smaller_head = array1 if array1[0] < array2[0] else array2
    return smaller_head.pop(0)

print merge_sort([0, 1, 2, 3, 4])
print merge_sort([1, 3, 5, 2, 4, 6])

random_array = [random.randint(0, 100) for i in range(100)]


print sorted(random_array) == merge_sort(random_array)
