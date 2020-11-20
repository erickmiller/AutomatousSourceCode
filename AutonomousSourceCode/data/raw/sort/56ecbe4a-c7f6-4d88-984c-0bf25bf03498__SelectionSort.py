from time import time

__author__ = 'rabbi'


class SelectionSort:
    def __init__(self, unSortedList):
        self.unSortedList = unSortedList

    def selectionSort(self):
        """
        Selection Sort
        """
        for fillSlot in range(len(self.unSortedList) - 1, 0, -1):
            positionMax = 0
            for location in range(1, fillSlot + 1):
                if self.unSortedList[location] > self.unSortedList[positionMax]:
                    positionMax = location
            temp = self.unSortedList[fillSlot]
            self.unSortedList[fillSlot] = self.unSortedList[positionMax]
            self.unSortedList[positionMax] = temp

        return self.unSortedList


if __name__ == '__main__':
    unSortedList = [12, 10, 8, 5, 9, 13, 20, 18, 17, 2, 4, 5, 1]
    selectionSort = SelectionSort(unSortedList)
    startTime = time()
    sortedList = selectionSort.selectionSort()
    endTime = time()
    print sortedList
    print "Execution Time: %f" % (endTime - startTime)
