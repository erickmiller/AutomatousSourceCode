class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        s_list, t_list = list(s), list(t)
        s_list.sort()
        t_list.sort()
        sorted_s = ''.join(s_list)
        sorted_t = ''.join(t_list)
        return sorted_s == sorted_t