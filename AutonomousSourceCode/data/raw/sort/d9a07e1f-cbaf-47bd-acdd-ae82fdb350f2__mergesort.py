class MergeSort:

    def __init__(self):
        pass

    def mergeSort(self, argList):

        sortedList = []

        if len(argList) == 1:
            return argList

        mid = int(len(argList)/2)
        sortedLeftList = self.mergeSort(argList[:mid])
        sortedRightList = self.mergeSort(argList[mid:])

        leftIndex = 0
        rightIndex = 0
        listIndex = 0


        #Sorts in increasing order
        while leftIndex < len(sortedLeftList) and rightIndex < len(sortedRightList):
            if sortedLeftList[leftIndex] > sortedRightList[rightIndex]:
                sortedList += [sortedRightList[rightIndex]]
                rightIndex += 1
            else:
                sortedList += [sortedLeftList[leftIndex]]
                leftIndex += 1

        sortedList += sortedLeftList[leftIndex:]
        sortedList += sortedRightList[rightIndex:]

        return sortedList


if __name__ == "__main__":

    toBeSortedList = [5,3,8,2,1,9,7]
    sorter = MergeSort()
    myList = sorter.mergeSort(toBeSortedList)
    print myList