def selection_sort(A):

    for i in range(len(A)):
        minval = float("inf")
        minindx = -1
        for j in range(i,len(A)):
            if A[j] < minval:
                minval = A[j]
                minindx = j
        A[i], A[minindx] = A[minindx], A[i]

    return A

assert selection_sort([4,8,3,7,2,6,1,5,0]) == sorted([4,8,3,7,2,6,1,5,0])

