__author__ = 'bruno'


def odd_even_sort(unordered):
    """
        Worst case O(n^2)
        Best case O(n)
        Worst case space O(1)
    """
    is_sorted = False
    while not is_sorted:
        is_sorted = True

        i = 1
        while i < len(unordered)-1:
            if unordered[i] > unordered[i+1]:
                unordered[i], unordered[i+1] = unordered[i+1], unordered[i]
                is_sorted = False
            i += 2

        i = 0
        while i < len(unordered)-1:
            if unordered[i] > unordered[i+1]:
                unordered[i], unordered[i+1] = unordered[i+1], unordered[i]
                is_sorted = False
            i += 2
    return unordered