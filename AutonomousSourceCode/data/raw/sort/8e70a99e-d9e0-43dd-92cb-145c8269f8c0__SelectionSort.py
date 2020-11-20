##############################################################################################################################
#      Project:                  Selection Sort
#      Time Complexity:          O(n2)  
#      Space Complexity:         O(1)
#      Stability:                Not stable
#      Info:                     Decrease-by-one sorting
##############################################################################################################################

# Selection Sort          
def SelectionSort(L):
	unsorted_list = L
	sorted_list = []
	while unsorted_list != []:
		least = unsorted_list[0]
		for e in unsorted_list:
			if e < least:
				least = e
		unsorted_list.remove(least)
		sorted_list.append(least)
	return sorted_list

##############################################################################################################################

# In-place Selection Sort  
def Inplace_SelectionSort(L):
	for i in range(len(L)):
		l = i
		for j in range(i+1, len(L)):
			if L[j] < L[l]:
				l = j
		#swap L[i] and L[l]
		L[l], L[i] = L[i], L[l]

##############################################################################################################################

def main():
	L1 = [1, 4, 3, 5, 6, 2]
	print "SelectionSort: ", SelectionSort(L1)

	L2 = [1, 4, 3, 5, 6, 2]
	Inplace_SelectionSort(L2)
	print "Inplace SelectionSort: ", L2

if __name__ == '__main__':
	main()	