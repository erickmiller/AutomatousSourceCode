class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        numSorted=[item for item in num]
        numSorted.sort()
        length=len(numSorted)
        left=0
        right=length-1
        while left<right:
            if numSorted[left]+numSorted[right]<target:
                left+=1
            elif numSorted[left]+numSorted[right]>target:
                right-=1
            else:
                break
        i=0
        j=0
        for i in range(length):
            if num[i]!=numSorted[left]:
                i+=1
            else:
                break
        for j in range(length):
            if num[j]!=numSorted[right]:
                j+=1
            elif j==i:
                continue
            else:
                break
        if i>j:
            return (j+1,i+1)
        return (i+1,j+1)

a=Solution()
b=a.twoSum([1,6,5,3,4],9)
print(b)