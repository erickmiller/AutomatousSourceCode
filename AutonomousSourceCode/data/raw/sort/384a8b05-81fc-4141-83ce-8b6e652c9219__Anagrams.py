class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        res = {}
        for x in strs:
            sort_x = ''.join(sorted(x))
            if sort_x in res:
                res[sort_x] += [x]
            else:
                res[sort_x] = [x]
        s = []
        for x in res:
            if len(res[x]) >= 2:
                s += res[x]
        return s    