class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if len(nums) == 0:
            return False
            
        sorted_array = []
        for idx in range(len(nums)):
            sorted_array.append((idx, nums[idx]))
            
        sorted_array.sort(key=lambda x: x[1])
        
        for each in range(len(nums)):
            target = each+1
            
            while target < len(nums) and sorted_array[target][1] - sorted_array[each][1] <= t:
                if abs(sorted_array[target][0] - sorted_array[each][0]) <= k:
                    return True
                else:
                    target += 1
        
        return False