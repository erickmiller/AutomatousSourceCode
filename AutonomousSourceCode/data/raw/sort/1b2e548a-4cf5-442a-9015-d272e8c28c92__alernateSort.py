def alternateSort(ar):
	sorted(ar)
	for i in range(1,len(ar),2):
		if i!=len(ar)-1:
			temp = ar[i]
			ar[i]=ar[i+1]
			ar[i+1]=temp
	return ar

print alternateSort([1,2,3,4,5,6,7])
