class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str in strs:
            sortedStr = ''.join(sorted(str))
            if dic.has_key(sortedStr):
                dic[sortedStr].append(str)
            else:
                dic[sortedStr] = [str]
            
        result = []
        for key, val in dic.iteritems():
            val.sort()
            result.append(val)
        return result