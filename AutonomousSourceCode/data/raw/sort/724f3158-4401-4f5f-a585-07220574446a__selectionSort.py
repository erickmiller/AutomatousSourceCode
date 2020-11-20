def selectionSort(L):
    sorted = []
    remaining = L
    while len(remaining) > 0:
        lowest = remaining[0]
        for x in remaining:
            if x < lowest:
                lowest = x
        sorted.append(lowest)
        remaining.remove(lowest)
    return sorted


list1 = [65, 23, 74, 87, 9, 34, 143]
print list1
print selectionSort(list1)
