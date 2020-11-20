from numpy import array,append,zeros,ones,amin
#import sys

def dictionaryRead(input_files):

    lines = open(input_files).readlines()
    lines = [line.rstrip().split() for line in lines if line.strip()]

    for line in lines:
        for i in range(len(line)):
            #print line[i]
            line[i] = float(line[i])

    dictSort = [lines[0]]
    dictSort.append(sorted(lines[1]))
    b0_sortedIndex = sorted(range(len(lines[1])), key = lambda k: lines[1][k])
    b0_sorted = [lines[3][idx] for idx in b0_sortedIndex]
    dictSort.append(sorted(lines[2]))
    nonBasicCoeIndex=sorted(range(len(lines[2])), key=lambda k: lines[2][k])
    dictSort.append(b0_sorted)
    size_constraints=int(lines[0][0])
    for i in b0_sortedIndex:
        coeSorted=[lines[i+4][idx] for idx in nonBasicCoeIndex]
        dictSort.append(coeSorted)
        
    objSorted=[lines[-1][0]]
    tmp=[lines[-1][idx+1] for idx in nonBasicCoeIndex]
    objSorted.extend(tmp)
    dictSort.append(objSorted)


    return dictSort
