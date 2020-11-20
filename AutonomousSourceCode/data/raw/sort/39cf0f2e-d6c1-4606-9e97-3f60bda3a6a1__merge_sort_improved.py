# Merge Sort


def merge(left, right):
    """Merges two sorted lists.
    Args:
        left: A sorted list.
        right: A sorted list.

    Returns:
        The sorted list resulting from merging the two sorted sublists.

    Requires:
        left and right are sorted.
    """

    items = []

    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            items.append(left[i])
            i = i + 1
        else:
            items.append(right[j])
            j = j + 1

    if i < len(left):
        items.extend(left[i:])
    elif j < len(right):
        items.extend(right[j:])

    return items


def merge_sort(items):
    """Sorts a list of items.

    Uses merge sort to sort the list items.
    
    Args:
        items: A list of items.

    Returns:
        The sorted list of items. 
    """
    n = len(items)
    if n < 2:
        return items

    m = n // 2
    left = merge_sort(items[:m])
    right = merge_sort(items[m:])
    return merge(left, right)
