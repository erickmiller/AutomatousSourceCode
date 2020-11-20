# Bubble Sort: Sorting an array using Bubble Sort

# Based on http://en.wikipedia.org/wiki/Bubble_sort#Optimizing_bubble_sort's pseudocode
def bubble_sort(A):
	n = len(A)
	while True:
		newn = 0
		i = 1
		while i <= (n - 1):
			if A[i - 1] > A[i]:
				A[i - 1], A[i] = A[i], A[i - 1]
				newn = i
			i += 1
		n = newn
		if n == 0:
			break
	
	return A

def main():
	arr = [8, 6, 7, 5, 3, 0, 9]
	sorted = [0, 3, 5, 6, 7, 8, 9]
	
	print("Output:", bubble_sort(arr))
	print("Expected:", sorted)

if __name__ == "__main__":
	main()