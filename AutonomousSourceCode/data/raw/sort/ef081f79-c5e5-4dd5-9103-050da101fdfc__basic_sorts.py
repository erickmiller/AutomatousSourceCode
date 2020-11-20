from heap import Heap

def insertion_sort(array):
	"""
	Standard insertion sort alogrithm
	
	Arguments:
		array - array of numbers

	Returns:
		array - array sorted in increasing order
	"""

	for i in range(1, len(array)):
		j = i - 1
		while j >= 0 and array[j] > array[i]:
			array[i], array[j] = array[j], array[i]
			i = j
			j-=1

	return array

def selection_sort(array):
	"""
	Standard selection sort algorithm.

	Arguments:
		array - array of numbers

	Returns:
		array - array sorted in increasing order
	"""

	for i in range(0, len(array)-1):

		min_index = None

		for j in range(i, len(array)):

			if not min_index:
				min_index = j
			else:
				if array[j] < array[min_index]:
					min_index = j
		array[i], array[min_index] = array[min_index], array[i]

	return array

def merge(array1, array2):
	"""
	Take two sorted arrays and merge them in sorted order.

	Arguments:
		array1 - first array to be sorted
		array2 - second array to be sorted

	Returns:
		sorted_array - merged arrays in sorted manner
	"""

	sorted_array = []
	while array1 and array2:
		if array1[0] < array2[0]:
			sorted_array.append(array1.pop(0))
		else:
			sorted_array.append(array2.pop(0))

	if not array1:
		sorted_array.extend(array2)
	elif not array2:
		sorted_array.extend(array1)

	return sorted_array

def merge_sort(array):
	"""
	Merge sort a given array in ascending order

	Arguments:
		array - potentially unsorted array

	Returns:
		sorted_array - sorted array in ascending order
	"""
	if len(array) == 1 or not array:
		return array

	else:
		sorted_array = merge(merge_sort(array[0:len(array)/2]), merge_sort(array[len(array)/2:]))

	return sorted_array

def quick_sort(array, start=0, end=None):
	"""
	Perform a quick sort in place

	Arguments:
		array - array to be sorted
		start - starting index of array to be sorted
		end - end index of array to be sorted

	Returns:
		array - sorted array
	"""

	if not array:
		return

	if not end:
		end = len(array)-1

	pivot = end
	curr_index = start

	while curr_index != pivot:
		if array[curr_index] > array[pivot]:
			array[curr_index], array[pivot-1] = array[pivot-1], array[curr_index]
			array[pivot-1], array[pivot] = array[pivot], array[pivot-1]
			curr_index = start
			pivot-=1
		else:
			curr_index+=1

	if pivot - start > 1:
		quick_sort(array, start, pivot-1)
	if pivot < end-2:
		quick_sort(array, pivot + 1, end)

	return array

def heap_sort(array):
	"""
	Performs a heap sort

	Arguments:
		array - array of integers to be sorted

	Returns:
		array - sorted array
	"""

	sorted_array = []
	array_heap = Heap(array)

	while array_heap.size > 0:
		sorted_array.append(array_heap.remove())

	return sorted_array