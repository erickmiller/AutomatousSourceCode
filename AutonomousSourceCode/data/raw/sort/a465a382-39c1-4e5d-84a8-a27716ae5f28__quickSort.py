
def partition(p,r):
	q = p
	for u in xrange(p,r):
		if A[u] <= A[r]:
			A[q], A[u] = A[u], A[q]
			q = q + 1
	A[q],A[r] = A[r],A[q]
	return q



def quickSort(p,r):
	if p<r:
		q = partition(p,r)
		quickSort(p,q-1)
		quickSort(q+1,r)


if __name__ == "__main__":
	N = int(raw_input())
	global A
	A = []
	for i in xrange(N):
		A.append(raw_input())
	quickSort(0,N-1)
	print "\nThe sorted list is: ", A
