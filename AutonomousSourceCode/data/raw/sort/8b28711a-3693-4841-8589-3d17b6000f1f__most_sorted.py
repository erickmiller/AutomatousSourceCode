#create a mostly sorted list
#creates a sorted list, then switches the ends.

def MostlySortedList(n):
	A = CreateRandomList(N) 
	A.sort()
	A[0], A[-1] = A[-1], A[0]
	return A