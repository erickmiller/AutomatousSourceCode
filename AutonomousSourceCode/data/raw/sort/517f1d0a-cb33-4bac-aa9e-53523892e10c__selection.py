#selection sort
def select_sort(nums):
	size = len(nums)
	for i in range(0,size-1):
		min_element = i
		for j in range(i+1,size):
		  if(nums[j]<nums[min_element]):
		        min_element = j
	        temp = nums[min_element]
                nums[min_element] = nums[i]
	        nums[i] = temp
	return nums

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
	sorted_nums = select_sort(nums)
	#print the sorted list
	print "sorted numbers: "
	display_result(sorted_nums)

