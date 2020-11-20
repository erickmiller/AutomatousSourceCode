def median(seq):
    sort = sorted(seq[:])
#    print sort
    size = len(seq)
    half = size // 2
#    print seq[half]
    result = 0
    if size % 2 == 0:
        result = (sort[half-1] + sort[half]) / 2.0
    else:
        result = sort[half]
    return result

    
print median([5,2,4,7,4,9])
print median([6, 8, 12, 2, 23])
