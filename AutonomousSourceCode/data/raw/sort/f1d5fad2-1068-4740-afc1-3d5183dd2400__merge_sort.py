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
	
def get_input():
	a=[]
	while(1):
	  x = int(raw_input())
	  if(x==-1):
	     break
	  a.append(x)
        return a
	
def display_result(sorted_nums):
	print sorted_nums


if __name__ == '__main__':
	#get input from user
	print "enter the numbers to be sorted and -1 to exit "
	nums = get_input()
	#sort the list
	sorted_nums = merge_sort(nums)
	#print the sorted list
	print "sorted numbers: "
	display_result(sorted_nums)