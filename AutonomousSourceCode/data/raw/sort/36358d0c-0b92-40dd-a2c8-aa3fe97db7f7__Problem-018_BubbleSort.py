def swap(x1,x2):return x2,x1

def bubbleSort(lst):
	correctlySorted = False
	while not correctlySorted:
		correctlySorted = True
		for idx in range(len(lst) - 1):
			if lst[idx] > lst[idx + 1]: correctlySorted = False ; lst[idx],lst[idx + 1] = swap(lst[idx], lst[idx + 1])
	return lst

print bubbleSort([4,2,3,1])							
			
	
