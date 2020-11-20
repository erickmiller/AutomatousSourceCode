'''
Implement int sqrt(int x).
.
Compute and return the square root of x.
'''

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        l = 0;   h = x+1
        while l <= h:
            m = (l + h) / 2
            if m ** 2 <= x < (m + 1) ** 2:      return m
            elif x < m ** 2:   h = m - 1
            else:    l = m + 1