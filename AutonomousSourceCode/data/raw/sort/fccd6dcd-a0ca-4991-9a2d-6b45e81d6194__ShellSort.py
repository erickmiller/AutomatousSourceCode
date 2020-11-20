import random
from time import time

__author__ = 'rabbi'


class ShellSort:
    def __init__(self, unSortedList):
        self.unSortedList = unSortedList

    def shellSort(self):
        """
        Shell Sort
        """
        gap = len(self.unSortedList) // 2
        # loop over the gaps
        while gap > 0:
            # do the insertion sort
            for i in range(gap, len(self.unSortedList)):
                val = self.unSortedList[i]
                j = i
                while j >= gap and self.unSortedList[j - gap] > val:
                    self.unSortedList[j] = self.unSortedList[j - gap]
                    j -= gap
                self.unSortedList[j] = val
            gap //= 2

        return self.unSortedList


if __name__ == '__main__':
    unSortedList = [12, 10, 8, 5, 9, 13, 20, 18, 17, 2, 4, 5, 1]
    for i in range(100000):
        unSortedList.append(random.randint(1, 50000))
    shellSort = ShellSort(unSortedList)
    startTime = time()
    sortedList = shellSort.shellSort()
    endTime = time()
    print sortedList
    print "Execution Time: %f" % (endTime - startTime)
