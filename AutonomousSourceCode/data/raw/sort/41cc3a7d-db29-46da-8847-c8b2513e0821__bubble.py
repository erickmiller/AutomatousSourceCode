#Sort the numbers using bubble sort
def bubble_sort(nums):
        n=len(nums)
        for i in range(0,n):
            for j in range(0,n-i-1):
                if nums[j]>nums[j+1]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
        return nums

def input_num():
        a=[]
        print'Enter the array elements\npress -1 when you are done with the inputs'
        while(1):
            x=int(raw_input())
            if x==-1:
                break
            a.append(x)

        return a

    #unsorted array
nums=input_num()
    #call bubble sort
sort_num=bubble_sort(nums)
    #print the sorted array
print 'The sorted array is\n'
print sort_num            
