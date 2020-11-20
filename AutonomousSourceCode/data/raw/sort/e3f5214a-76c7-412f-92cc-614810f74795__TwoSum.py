class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        sort_num = sorted(nums)
        i = 0
        j = len(sort_num) - 1
        
        while i < j: 
            diff = sort_num[i] + sort_num[j] - target 
            if diff == 0:
                index1 = nums.index(sort_num[i])+1
                
                index2 = len(nums) - nums[::-1].index(sort_num[j])
                return sorted([index1, index2])
            elif diff < 0:  
                i = i + 1
            else:
                j = j - 1
                
        return []
        