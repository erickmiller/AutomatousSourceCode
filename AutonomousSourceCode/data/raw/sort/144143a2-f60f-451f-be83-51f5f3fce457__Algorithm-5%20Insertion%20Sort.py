def insertion_sort(L):
	"""Returns a Sorted List.
	Usage:
	>>>insertion_sort([6,8,1,8,3])
	>>>[1, 3, 6, 8, 8]
	"""
	n = len(L)
	for j in range(1,n):
		 i = 0
		 while L[j] > L[i]:
		 	i += 1
		 m = L[j]
		 for k in range(0,j-i):
		 	L[j-k] = L[j-k-1]
		 L[i] = m
	return L

print insertion_sort([6,8,1,8,3])
