#insertion sort
def insert_sort(nums):
	size = len(nums)
	for index in range(1,size):
		value = nums[index]
		i = index-1
		while(i>=0):
		  if(value < nums[i]):
		    nums[i+1]=nums[i]
		    nums[i]=value
		    i=i-1
		  else:
                    break
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
	sorted_nums = insert_sort(nums)
	#print the sorted list
	print "sorted numbers: "
	display_result(sorted_nums)

