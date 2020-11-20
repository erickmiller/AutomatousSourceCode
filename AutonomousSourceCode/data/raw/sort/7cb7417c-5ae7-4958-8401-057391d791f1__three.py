#Given the array arr, return the array sorted
#Example: given [1, 3, 4, 2, 5] return [1, 2, 3, 4, 5]

#Run with: python test.py three
def sort(arr):
    #Your code goes here
	sorted = False
	while not sorted:
		sorted = True
		for i in range(0, len(arr)-1):
			if arr[i] > arr[i+1]:
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
				sorted = False
	print arr
	return arr
