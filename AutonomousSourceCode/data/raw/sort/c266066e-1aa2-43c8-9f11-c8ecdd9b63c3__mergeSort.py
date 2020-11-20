

def mergeSort(listNums, startPtr, endPtr):
	if (startPtr > endPtr) or (startPtr < 0)  or (endPtr >= len(listNums)):			## check argument for special cases / errors
		return []	
	elif startPtr == endPtr:									## base case. list with individual element is always sorted
		return [listNums[startPtr]]
	
	midPtr = (startPtr+endPtr)/2								## divide lists in two parts
	sortedLeft = mergeSort(listNums, startPtr, midPtr)			## sort left part and right part individually
	sortedRight = mergeSort(listNums, midPtr+1, endPtr)
	
	sortedList = merge(sortedLeft, sortedRight)					## combine the two sorted lists
	# print sortedLeft, sortedRight, sortedList

	return sortedList


def merge(sortedLeft, sortedRight):
	if (not sortedLeft) and (not sortedRight):
		return []
	elif not sortedLeft:
		return sortedRight
	elif not sortedRight:
		return sortedLeft
	else:
		leftPtr = 0
		rightPtr = 0
		sortedList = []
		while (leftPtr < len(sortedLeft)) and (rightPtr < len(sortedRight)):
			leftNum = sortedLeft[leftPtr]
			rightNum = sortedRight[rightPtr]
			if leftNum <= rightNum:
				sortedList.append(leftNum)
				leftPtr += 1
			else:
				sortedList.append(rightNum)
				rightPtr += 1
		sortedList.extend(sortedLeft[leftPtr:])		## append sorted list with both lists (only one at most would be non-empty)
		sortedList.extend(sortedRight[rightPtr:])	## and it would automatically be sorted, so we just need to copy paste the elements

	return sortedList



listNums = [2,5,1,6]
N = len(listNums)
print "\noriginal list: {}".format(listNums)
sortedList = mergeSort(listNums, 0, N-1)
print "sorted list: {}\n".format(sortedList)
