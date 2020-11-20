""" sorting algorithms here"""

def merge_sort(array = [6,3,6,3,21,7,3,4,5,3,1]):

	if len(array) <= 1:
		return array
	mid_index = len(array)//2;
	sorted_left = merge_sort(array[:mid_index])
	sorted_right = merge_sort(array[mid_index:])
	print sorted_left
	print sorted_right
	sorted_array = []
	# join right and left arrays
	while sorted_left or sorted_right:
		if not sorted_left:
			sorted_array += sorted_right
			sorted_right = []
		elif not sorted_right:
			sorted_array += sorted_left
			sorted_left = []
		else:
			if sorted_left[0] < sorted_right[0]:
				sorted_array.append(sorted_left.pop(0))
			else:
				sorted_array.append(sorted_right.pop(0))
	return sorted_array

def merge_sort_indexed(array = [6,3,6,3,21,7,3,4,5,3,1]):
	print 'todo'


def quicksort(array = [6,3,6,3,21,7,3,4,5,3,1]):
	print 'todo'


""" searching algorithms here """
def binary_search(array = [1,2,3,4,5,6,7,8,9], value = 8, left = 0, right = 8):
	print 'left: '+ str(left) + ', right: '+ str(right)
	if left > right:
		return -1
	if left == right:
		if array[left] == value:
			return left
		else:
			return -1


	middle_index = left + (right-left)//2
	if array[middle_index] == value: 
		return middle_index
	elif array[middle_index] > value:
		return binary_search(array, value, left, middle_index-1)
	else:
		return binary_search(array, value, middle_index+1, right)


if __name__ == "__main__":
	# sorted_array = merge_sort()
	# print sorted_array
	print binary_search()


