def merge(list1, list2):
  i = 0
  j = 0
  output = []
  len1 = len(list1)
  len2 = len(list2)
  while i < len1 or j < len2:
    
    if i < len1 and j < len2:
      if list1[i] < list2[j]:
        
        output += [list1[i]]
        i = i+1
      else:
        
        output += [list2[j]]
        j = j+1
    
    elif i < len1:
      output += [list1[i]]
      i = i+1
    
    elif j < len2:
      output += [list2[j]]
      j = j+1
  return output
def merge_sort(list):
  length = len(list)
  
  if length <= 1:
    return list
  
  else:
    
    mid = length/2
    left = list[0:mid]
    right = list[mid:]
    
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    
    return merge(sorted_left, sorted_right)
def get_data():
	nums=[]
	while True:
		a=int(raw_input("Enter a number (-1 to exit) : "))
		if a==-1:
			break
		nums.append(a)
	return nums

if __name__=='__main__':
	nums=get_data()
	print "Input data is : ",nums
	print "Sorted data is : ",merge_sort(nums)
