def mergeTwoSortedArray(a, b):
	n1, n2 = len(a), len(b)
	n = n1 + n2
	i, j, k = 0, 0, 0
	res = [None for x in range(n)]
	while i < n1 and j < n2:
		if a[i] <= b[j]:
			res[k] = a[i]
			i += 1
		else:
			res[k] = b[j]
			j += 1
		k += 1
	if i < n1:
		res[k:] = a[i:]
	else:
		res[k:] = b[j:]
	return res

def mergeSort(a):
	n = len(a)
	if n < 2:
		return a
	half = int(n/2)
	left, right = a[:half], a[half:]
	return mergeTwoSortedArray(mergeSort(left), mergeSort(right))

	
	
	
	
	
	
	
	
	