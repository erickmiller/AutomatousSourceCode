
def swap_lis(lis, i):
	lis[i], lis[i + 1] = lis[i + 1], lis[i]
      	return 0
                  
def sort(lis, limit):
	for i in range(limit):
		[swap_lis(lis, j) if lis[j] > lis[j + 1] for j in range(limit)]  
	return lis


lis = input("enter the list\n")
limit = len(lis) - 1
lis_sorted = sort(lis, limit)
print "the sorted list is %r"%(lis_sorted)
		

