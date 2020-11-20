#!/usr/bin/python  
# -*- coding: utf-8 -*- 

"""
# soluction

"""
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        sorted_num = num[:]
        sorted_num.sort()   # increase
        l, r = 0, len(sorted_num)-1
        while l<r:
            if sorted_num[l]+sorted_num[r]==target:
                break;
            elif sorted_num[l]+sorted_num[r]<target:
                l += 1;
            else:
                r -= 1;
        index1, index2 = 1, 1
        if sorted_num[l]+sorted_num[r]==target: # note the order
            for i in xrange(len(num)):
                if num[i]==sorted_num[l] or num[i]==sorted_num[r]:
                    index1, index2 = index2, i+1
        return (index1, index2)
    
    # @return a tuple, (index1, index2)
    def twoSum1(self, num, target):
        # take use of hash
        mapping = {}
        for i in xrange(len(num)):
            if mapping.has_key(target-num[i]):
                return (mapping[target-num[i]], i+1)
            mapping[num[i]] = i+1
        return (0, 0)
        

if __name__ == '__main__':
    pass
