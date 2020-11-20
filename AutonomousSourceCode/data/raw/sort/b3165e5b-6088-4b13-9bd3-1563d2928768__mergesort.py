#!/usr/bin/python

def mergeSort(arrayForSort):
    if(len(arrayForSort) == 1):
        return arrayForSort
    else:
        length = len(arrayForSort)
        firstSortedArray = mergeSort(arrayForSort[:length/2])
        secondSortedArray = mergeSort(arrayForSort[length/2:])
        sortedArray = mergeTwoArrays(firstSortedArray, secondSortedArray)
        return sortedArray

def mergeTwoArrays(first, second):
    firstArrayIndex = 0
    secondArrayIndex = 0
    resultArray = []

    while (True):
        if(first[firstArrayIndex] <= second[secondArrayIndex]):
            resultArray.append(first[firstArrayIndex])
            firstArrayIndex = firstArrayIndex + 1
        else:
            resultArray.append(second[secondArrayIndex])
            secondArrayIndex = secondArrayIndex + 1

        if(firstArrayIndex == len(first)):
            resultArray.extend(second[secondArrayIndex:])
            break;

        if(secondArrayIndex == len(second)):
            resultArray.extend(first[firstArrayIndex:])
            break;

    return resultArray


array = [3,41,52,26,38,57,9,49]
resultArray = mergeSort(array)
print resultArray
