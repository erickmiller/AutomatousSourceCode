class QuickSort:

    def __init__(self):
        pass
	
	def quickSort(self,listToSort,low,high):
		if low < high:
			pivotIndex = partition(listToSort,low,high)
			quickSort(listToSort,low,pivotIndex-1)
			quickSort(listToSort,pivot+1,high)
			
	def partition(self,listToSort,low,high):
		pivot = listToSort[high]
		i = low
		j = low
		while j < high-1:
			if listToSort[j] <= pivot:
				value = listToSort[j]
				listToSort[j] = listToSort[i]
				listToSort[i] = value
				i += 1
		value = listToSort[high]
		listToSort[high] = listToSort[i]
		listToSort[i] = value
		return i
	
if __name__ == "__main__":

    toBeSortedList = [5,3,8,2,1,9,7]
    sorter = QuickSort()
    myList = sorter.quickSort(toBeSortedList,0,len(toBeSortedList)-1)
    print myList