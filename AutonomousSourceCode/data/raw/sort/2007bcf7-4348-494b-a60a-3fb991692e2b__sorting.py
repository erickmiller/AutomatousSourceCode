def selection_sort(l):
    sorted = []
    while l:
        sorted.append(min(l))
        l.remove(l)
    return sorted

