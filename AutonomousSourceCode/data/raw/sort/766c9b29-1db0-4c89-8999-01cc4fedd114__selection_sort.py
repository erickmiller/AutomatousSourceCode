
seq = [7, 13, 2, -1, -1, 16]

def selection_sort(sequence):
    seqLen = len(sequence)
    sortedSeq = sequence[:]
    
    for i in range(0, seqLen-1):
        minIdx=i
        for k in range(i+1, seqLen):
            if sortedSeq[k] < sortedSeq[minIdx]:
                minIdx = k
        sortedSeq[i], sortedSeq[minIdx] = sortedSeq[minIdx], sortedSeq[i]
    
    return sortedSeq
    
print selection_sort(seq)


#sort function in python has complexity of O(nlogn)
