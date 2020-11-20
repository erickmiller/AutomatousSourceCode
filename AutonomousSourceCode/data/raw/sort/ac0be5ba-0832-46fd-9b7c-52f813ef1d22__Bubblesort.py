__author__ = 'Meemaw'



def bubbleSort(aList):
    for i in range(1,len(aList)):
        sorted = True
        for j in range(len(aList)-i):
            if aList[j] > aList[j+1]:
                sorted = False
                aList[j], aList[j+1] = aList[j+1], aList[j]
        if sorted:
            return

