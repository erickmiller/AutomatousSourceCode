class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        s_sort = ''.join(sorted(s))
        t_sort = ''.join(sorted(t))
        return True if s_sort == t_sort else False
