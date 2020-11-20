class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        n = len(nums)
        sorted_nums = self.merge_sort(nums)
        return sorted_nums[n-k]
        
    
    def merge_sort(self, nums):
        n = len(nums)
        if n == 0 or n == 1:
            return nums
        mid = n/2
        left_nums = self.merge_sort(nums[0:mid])
        right_nums = self.merge_sort(nums[mid:])
        print left_nums,right_nums
        sorted_nums = self.merge(left_nums, right_nums)
        
        return sorted_nums
    
    def merge(self,left_nums,right_nums):
        print left_nums,right_nums
        nl = len(left_nums)
        nr = len(right_nums)
        left_nums.append(float('inf'))
        right_nums.append(float('inf'))
        sorted_nums = []
        i = 0
        j = 0
        k = 0
        while k < nl + nr:
            if left_nums[i] < right_nums[j]:
                sorted_nums.append(left_nums[i])
                i += 1
                k += 1
            elif left_nums[i] == right_nums[j]:
                sorted_nums.append(left_nums[i])
                i += 1
                j += 1
                k += 2
            else:
                sorted_nums.append(left_nums[j])
                j += 1
                k += 1
        print sorted_nums
        return sorted_nums
                
nums = [7,6,5,4,3,2,1]
k = 2
sol =Solution()
print sol.findKthLargest(nums,k)           
        