def setify(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

def second_largest(numbers):
    result = 0
    sorted_numbers = sorted(numbers)
    unique_sort_numbers = setify(sorted_numbers)
    pre_last_index = len(unique_sort_numbers) -2
    if len(unique_sort_numbers) < 2:
        return False
    result = unique_sort_numbers[pre_last_index]
    return result
a = [1,3,5,6,7,6,2,1,200, 800, 13]
b = [4,4]
c = [10,10,10,10,9]
print(second_largest(a))
print(second_largest(b))
print(second_largest(c))