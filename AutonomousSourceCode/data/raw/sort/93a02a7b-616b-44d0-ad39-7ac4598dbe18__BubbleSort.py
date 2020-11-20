from time import time

__author__ = 'rabbi'


class BubbleSort:
    def __init__(self, unSortedList):
        self.unSortedList = unSortedList

    def bubbleSort(self):
        """
        Bubble sort
        """
        for passedNumber in range(len(self.unSortedList) - 1, 0, -1):
            for i in range(passedNumber):
                if self.unSortedList[i] > self.unSortedList[i + 1]:
                    self.unSortedList[i], self.unSortedList[i + 1] = self.unSortedList[i + 1], self.unSortedList[i]
        return self.unSortedList


if __name__ == '__main__':
    unSortedList = [12, 10, 8, 5, 9, 13, 20, 18, 17, 2, 4, 5, 1]
    bubbleSort = BubbleSort(unSortedList)
    startTime = time()
    sortedList = bubbleSort.bubbleSort()
    endTime = time()
    print sortedList
    print "Execution Time: %f" % (endTime - startTime)