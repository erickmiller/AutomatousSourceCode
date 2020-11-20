def solution(A):
    len_a = len(A)
    if len_a < 3:
        return 0
        
    sort_a = sorted(A)
    for ind in xrange(0, len_a - 2):
        if (sort_a[ind] + sort_a[ind + 1]) > sort_a[ind + 2]:
            return 1
    return 0
