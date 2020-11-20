def insert(input, key):
    return [x for x in input if x <= key] + [key] + [x for x in input if x > key]

def insertSortRec(listToSort):
    if(len(listToSort) <= 1): return listToSort

    return insert(insertSortRec(listToSort[1:]), listToSort[0])

def insertSortIt(listToSort):
    sortedList = []
    for i in range(0,len(listToSort)):
        value = listToSort[i]
        sortedList = insert(sortedList, value)
    return sortedList

def insertSortInPlace(listToSort):
    for currentPos in range(1, len(listToSort)):
        currentValue = listToSort[currentPos]
        leftHandPos = currentPos-1
        while leftHandPos >= 0 and listToSort[leftHandPos] > currentValue:
            listToSort[leftHandPos + 1] = listToSort[leftHandPos]
            leftHandPos = leftHandPos -1
        listToSort[leftHandPos] = currentValue
    return listToSort
