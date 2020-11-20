def sort(unsorted):
    """Takes an unsorted list as input and returns 2 lenght n/2 unstored lists in a tuple."""
    if len(unsorted) < 2:
        return unsorted

    # split up list
    mid = len(unsorted) / 2
    left = unsorted[:mid]
    right = unsorted[mid:]

    # recursively split list to lengths of 1
    left = sort(left)
    right = sort(right)

    return merge(left, right)


def merge(left, right):
    """Takes 2 unsorted lists and returns 1 sorted list."""
    sorted = []

    i = 0
    j = 0
    for k in xrange(len(left) + len(right)):
        # if one side gets finished just extend the rest of the other sorted side
        if i == len(left):
            sorted.extend(right[j:])
            break
        elif j == len(right):
            sorted.extend(left[i:])
            break

        # append lesser of the 2 options
        if left[i] < right[j]:
            sorted.append(left[i])
            i = i + 1
        else:
            sorted.append(right[j])
            j = j + 1

    return sorted


def mergesort(unsorted):
    """Takes an unsorted list as imput and return a sorted list."""
    # if length of list is <= 1 it is already sorted
    if len(unsorted) <= 1:
        return unsorted

    return sort(unsorted)
