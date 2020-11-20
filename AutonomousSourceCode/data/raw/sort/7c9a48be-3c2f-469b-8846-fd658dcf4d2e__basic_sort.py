def min_elem(nums):
    min_index = 0

    index = 0
    for item in nums:
        if item < nums[min_index]:
            min_index = index

        index +=1           

    return min_index 

print(min_elem([3,-7,1,-4]))

def basic_sort (nums):
    sorted_nums = []

    while len(nums) != 0:
            min_index = min_elem(nums)
            sorted_nums = sorted_nums+ [nums[min_index]]
            del nums[min_index]
   
    return sorted_nums

print(basic_sort([2,3,0]))