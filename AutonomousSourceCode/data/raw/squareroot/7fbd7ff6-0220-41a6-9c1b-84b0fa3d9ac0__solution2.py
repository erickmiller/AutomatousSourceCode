# https://leetcode.com/problems/sqrtx/
'''
Implement int sqrt(int x).

Compute and return the square root of x.

Hide Tags Math Binary Search
'''
class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x < 0:
            return None
        if x == 0:
            return 0

        l = 0
        r = x
        while l <= r:
            m = (l + r) / 2
            if m * m == x:
                return m
            elif m * m < x and (m + 1) * (m + 1) > x:
                return m
            elif m * m < x:
                l = m + 1
            elif m * m > x:
                r = m - 1
