###############################################################################
"""
Question:
    LintCode: http://www.lintcode.com/en/problem/sqrtx/

    Implement int sqrt(int x).
    Compute and return the square root of x.
    Example
        sqrt(3) = 1
        sqrt(4) = 2
        sqrt(5) = 2
        sqrt(10) = 3

Analysis:
    Binary search. Find the last number which square of it <= x.
"""

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        start, end = 1, x
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid * mid <= x:
                start = mid
            else:
                end = mid
        if end * end <= x:
            return end
        else:
            return start