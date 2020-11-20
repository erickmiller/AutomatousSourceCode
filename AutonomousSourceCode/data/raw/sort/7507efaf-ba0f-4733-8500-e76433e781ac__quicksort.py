#!/usr/bin/python

myArray = [ 1, 50, 3, 17, 5, 3, 2, 99, 4 ]

def quickSort(arrayToSort):
  upper = []
  lower = []
  if len(arrayToSort) <= 1:
    return arrayToSort
  pivot = arrayToSort.pop()
  for elem in arrayToSort:
    if elem <= pivot:
      lower.append(elem)
    else:
      upper.append(elem)
  sortedArray = quickSort(lower)
  sortedArray.append(pivot)
  sortedArray.extend(quickSort(upper))
  return sortedArray

if __name__ == "__main__":
   print myArray
   print quickSort(myArray)
