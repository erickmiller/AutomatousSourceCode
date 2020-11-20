# -*- coding: utf8 -*-
'''
Given an array of strings, return all groups of strings that are anagrams.
Note: All inputs will be in lower-case.

For example:
Input:  ["tea","and","ate","eat","dan", "xyz"]
Output: ['and', 'dan', 'tea', 'ate', 'eat']
'''

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        def sort_str(string):
            l = list(string)
            l.sort()
            sorted_str = ""
            for c in l:
                sorted_str = sorted_str + c
            return sorted_str

        m = {}
        for string in strs:
            sorted_string = sort_str(string)
            if sorted_string in m:
                m[sorted_string].append(string)
            else:
                m[sorted_string] = [string]

        result = []
        for k in m:
            if len(m[k]) > 1:
                result = result + m[k]
        return result

if __name__ == "__main__":
    s = Solution()
    print s.anagrams(["tea","and","ate","eat","dan", "xyz"])

  
