##############################################################################################################################
#      Project:                  Merge Sort
#      Time Complexity:          O(nlogn)
#      Space Complexity:         O(n)
#      Stability:                Stable
#      Info:                     Decrease by half pattern (Divide and Conquer)
##############################################################################################################################

def Merge(A, B):
	S = []
	ai = 0
	bi = 0
	while len(A) > ai and len(B) > bi:
		if A[ai] <= B[bi]:
			x = A[ai]
			ai += 1
		else:
			x = B[bi]
			bi += 1
		S.append(x)
	return S + A[ai:] + B[bi:]

def MergeSort(L):
	if len(L) <= 1:
		return L
	else:
		half = int(len(L) / 2)
		A = L[:half]
		B = L[half:]
		return Merge(MergeSort(A), MergeSort(B))

##############################################################################################################################

def main():
	L = [2, 3, 5, 1, 7, 6, 8, 9, 10, 4]
	sorted_L = MergeSort(L)
	print "MergeSort: ", sorted_L

if __name__ == '__main__':
	main()	