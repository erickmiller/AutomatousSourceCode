def insertion_sort(seq):
	for i in range(1,len(seq)):
		j=i
		while j>0 and seq[j-1]>seq[j]:
			seq[j-1],seq[j]=seq[j],seq[j-1]
			j-=1
	return seq
seq=[3,5,2,6,8,1,0,3,5,6,2]
#print merge_sort(seq)
assert(insertion_sort(seq)==sorted(seq))