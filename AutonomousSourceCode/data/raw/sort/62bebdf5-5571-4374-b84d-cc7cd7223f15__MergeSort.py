import math
def MergeSort(unSorted):
    arrayLength = len(unSorted)
    if arrayLength == 1:
        return unSorted
    left  = [0 for i in range(math.floor(arrayLength / 2))]
    right = [0 for i in range(math.ceil(arrayLength / 2))]

    for i in range(math.floor(arrayLength / 2)):
        left[i] = unSorted[i]
        right[i] = unSorted[i + math.floor(arrayLength / 2)]

    # insert the last element in the right which is useful if the length of array is odd
    right[len(right) - 1] = unSorted[arrayLength - 1]
    left = MergeSort(left)
    right = MergeSort(right)

    return Merge(left , right)

def Merge(sortedA , sortedB):
    arrayLength = len(sortedA) + len(sortedB)
    result = [0 for i in range(arrayLength)]
    count , lenA , lenB = 0 , 0 , 0
    while(lenA < len(sortedA) and  lenB < len(sortedB)):
        if(sortedA[lenA] < sortedB[lenB]):
            result[count] = sortedA[lenA]
            lenA = lenA + 1
        else :
            result[count] = sortedB[lenB]
            lenB = lenB + 1
        count = count + 1
    if lenA < len(sortedA):
        while(lenA < len(sortedA)):
            result[count] = sortedA[lenA]
            lenA = lenA + 1
            count = count + 1
    if lenB < len(sortedB):
        while(lenB < len(sortedB)):
            result[count] = sortedB[lenB]
            lenB = lenB + 1
            count = count + 1
    return result


sortedArray = MergeSort([2,1,4,0,9,7,6, -8])
print(sortedArray)
