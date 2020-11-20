def bubble_sort(A):
  swapped = True # assume not sorted
  while swapped:
    swapped = False
    for i in range(1,len(A)):
      if A[i-1] > A[i]:
        A[i-1], A[i] = A[i], A[i-1]
        swapped = True
        print(A)
  return A

# main
A = [4, 5, 2, 1, 3]
print(bubble_sort(A))