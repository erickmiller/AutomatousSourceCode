import random

def isSorted(A):
	return all(A[i] <= A[i+1] for i in range(len(A)-1))

def sort(A):
	while not isSorted(A):
		random.shuffle(A)
	return A
