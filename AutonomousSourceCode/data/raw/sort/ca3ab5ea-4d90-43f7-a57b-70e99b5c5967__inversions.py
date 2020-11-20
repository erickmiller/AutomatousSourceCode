''' Short program to count inversions using merge sort as a basis.
    Input is numbers.txt
'''


def countSplitInversions(a, b):
  sortedA = []

  i = 0
  j = 0
  inversions = 0;

  while i < len(a) and j < len(b):
    if a[i] <= b[j]:
      sortedA.append(a[i])
      i += 1
    else:
      sortedA.append(b[j])
      j += 1
      inversions += len(a) - i
  if i == len(a):
    sortedA.extend(b[j:])
    
  if j == len(b):
    sortedA.extend(a[i:])

  return sortedA, inversions

def sortAndCountInversions(a):
  if len(a) <= 1:
    return (a, 0)

  leftIndex = int(len(a)/2) - 1
  rightIndex = leftIndex + 1
  leftSorted, leftInversions = sortAndCountInversions(a[0:leftIndex+1])
  rightSorted, rightInversions = sortAndCountInversions(a[rightIndex:])
  sortedA, splitInversions = countSplitInversions(leftSorted, rightSorted)
  return (sortedA, leftInversions + rightInversions + splitInversions)


# begin main program
with open("numbers.txt") as f:
 numbers = [[int(x) for x in line.split()] for line in f]

sortedNumbers, inversions = sortAndCountInversions(numbers)
print inversions
