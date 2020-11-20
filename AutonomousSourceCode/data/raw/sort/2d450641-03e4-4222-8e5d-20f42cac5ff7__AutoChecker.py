from Selection_sort import sort
import random
import os


def checker():
    sorted_elems = []
    result = []
    for i in range(10000):
        result.append(random.randint(0, 150000))

    sorted_elems = sort(result)
    length = len(sorted_elems)
    for i in range(length - 1):
        if sorted_elems[i] > sorted_elems[i + 1]:
            return False
    return True

print(checker())
