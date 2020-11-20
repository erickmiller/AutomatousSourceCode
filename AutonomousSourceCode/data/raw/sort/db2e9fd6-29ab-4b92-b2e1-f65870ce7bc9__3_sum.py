class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, arr):
        sorted_arr = sorted(arr)
        triplets = []
        result = []
        for i in range(len(sorted_arr)):
            for j in range(i + 1, len(sorted_arr)):
                for k in range(j + 1 , len(sorted_arr)):
                    if sorted_arr[i] + sorted_arr[j] + sorted_arr[k] == 0:
                        triplets.append([sorted_arr[i], sorted_arr[j], sorted_arr[k]])
        triplets.sort()
        for i in range(len(triplets)):
            if i == 0 or triplets[i] != triplets[i-1]:
                result.append(triplets[i])
        return result

solution = Solution()
print solution.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
