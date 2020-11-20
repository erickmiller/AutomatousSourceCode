# insertion sort
# ordered subarray, sort each element as you encounter it


def insert(array, splitIndex, value):
	"""
	insert value into array before item at splitIndex
	"""
	arr1 = array[0:splitIndex]
	arr2 = array[splitIndex:]
	return arr1 + [value] + arr2 


def index(x, sorted_a):
	"""
	returns splitIndex
	"""
	for elem in sorted_a:
		if x <= elem:
			return sorted_a.index(elem)
	else: 
		return len(sorted_a) # at the end

def insertSort(array):
	sorted_arr = [array[0]]
	for x in array[1:]:
		sorted_arr = insert(sorted_arr, index(x, sorted_arr), x)

	return sorted_arr


if __name__ == '__main__':
	print insert([0,1,2,3,4,5], 2, 10)	
	print insertSort([1,0,5,19,3,-16])