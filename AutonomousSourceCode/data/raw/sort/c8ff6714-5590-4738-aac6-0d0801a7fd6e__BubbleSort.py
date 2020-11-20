def BubbleSort(A):
	# does buble sort on array A returns the sorted list
	
	size=len(A)
	for i in range(size-1,0,-1):
		j=0
		while j<i:
		
			if A[j+1]<A[j]:
				A[j+1],A[j]=A[j],A[j+1]
			j=j+1
	
	return 



# For testing
A=[1,3,5,1,4,6,2,3,90,1,2,4,1,5,7,5,8,4,7]
BubbleSort(A)
print A
