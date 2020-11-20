def insert(list, n):
    isNmax = True
    try:
        a = next(list)
        while True:
            yield min(a, n)
            if a <= min(a, n):
                a = next(list)
            else:
                isNmax = False;
                while (True):
                    yield a
                    a = next(list)

    except StopIteration:
        if isNmax:
            yield n
        raise StopIteration


def insertionSort(list):
    sorted = iter([])
    for number in list:
        sorted = insert(sorted, number)
    return sorted


input = [0, 6, 7, 4, -3, 9, 100, 15, -22]

print(list(insertionSort(iter(input))))