import unittest

def merge_sort(array):
  if len(array) == 1:
    return array
  else:
    result = []
    first_sorted = merge_sort(array[:len(array)//2])
    second_sorted = merge_sort(array[len(array)//2:])
    while (len(first_sorted) and len(second_sorted)):
      result.append(first_sorted.pop(0)) if (first_sorted[0] <= second_sorted[0]) else result.append(second_sorted.pop(0))
    return result + first_sorted + second_sorted

    
def test(expected, actual): 
    sort = merge_sort(actual) 
    assert expected == sort 
    print actual, "is sort as", sort 
 
test([1], [1]) 
test([1, 2], [2, 1]) 
test([1, 2, 3], [2, 3, 1]) 
test([1, 2, 3, 4], [2, 3, 1, 4]) 
test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 6, 2, 3, 5, 1, 7, 4, 9, 8]) 
test([1, 1, 1, 2, 3, 4, 6, 7, 8, 8, 10], [10, 6, 7, 8, 8, 1, 1, 2, 1, 3, 4]) 

if __name__ == '__main__':
  unittest.main()