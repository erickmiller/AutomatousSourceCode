list = [9, 4, 6, 2, 3, 7, 8, 5, 1, 0]

def mergeSort(list):
	if(len(list) > 1):

		sortedList = []

		mid = len(list) // 2

		leftHalf = list[:mid]
		rightHalf = list[mid:]

		leftHalf = mergeSort(leftHalf)
		rightHalf = mergeSort(rightHalf)

		i = 0
		j = 0

		while(i < len(leftHalf) and j < len(rightHalf)):
			if(leftHalf[i] < rightHalf[j]):
				sortedList = sortedList + [leftHalf[i]]
				i = i + 1
			else:
				sortedList = sortedList + [rightHalf[j]]
				j = j + 1
		while(i < len(leftHalf)):
			sortedList = sortedList + [leftHalf[i]]
			i = i + 1
		while(j < len(rightHalf)):
			sortedList = sortedList + [rightHalf[j]]
			j = j + 1



		return sortedList
	else:
		return list


print(mergeSort(list))