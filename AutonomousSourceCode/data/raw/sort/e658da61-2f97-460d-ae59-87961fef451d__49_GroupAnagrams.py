'''
Created on 2015-08-30
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs.sort()
        d, result = dict(), []
        for s in strs:
            # Use this as key
            sorted_s = ''.join(sorted(s))
            if sorted_s not in d:
                d[sorted_s] = [s]
                result.append(d[sorted_s])
            else:
                d[sorted_s].append(s)
        return result

if __name__ == '__main__':
    pass