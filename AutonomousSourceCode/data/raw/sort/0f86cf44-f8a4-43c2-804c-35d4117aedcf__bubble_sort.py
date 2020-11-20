def bubble_sort(list):
	length = len(list) - 1
	sorted = False
	while not sorted:
		sorted = True
		for i in range(length):
			if list[i] > list[i+1]:
				(list[i], list[i+1]) = (list[i+1], list[i])
				# print list
				sorted = False
		length -= 1
	return list

unsorted = [6, 5, 3, 1, 8, 7, 2, 4]
print bubble_sort(unsorted)