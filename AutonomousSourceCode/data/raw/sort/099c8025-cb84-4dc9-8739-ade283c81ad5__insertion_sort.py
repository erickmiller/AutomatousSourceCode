def insertion_sort_desc(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        # Insert A[j] into the (desc) sorted sequence A[1..j-1]
        i = j - 1
        while (i >= 0) and (key > A[i]):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

    return A