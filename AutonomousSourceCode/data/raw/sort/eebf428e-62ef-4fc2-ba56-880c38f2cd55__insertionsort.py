def insertionsort(L):
	return calInsertionsort(L, 0)
	
def calInsertionsort(L, sortedIdx):
	if sortedIdx + 1 == len(L):
		return L
	
	sortData = L[sortedIdx+1]
	
	for idx in xrange(0, sortedIdx + 1):
		if sortData < L[idx]:
			del L[sortedIdx+1]
			L.insert(idx, sortData)
			break
		
	return calInsertionsort(L, sortedIdx+1)