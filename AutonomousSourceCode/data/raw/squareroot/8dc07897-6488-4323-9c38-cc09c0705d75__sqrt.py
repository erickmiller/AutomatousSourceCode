'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''


class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x < 0:
            return
        if x == 0 or x == 1:
            return x
        s, end, res = 1, x, 1
        while s <= end:
            mid = (s + end)/2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                s = mid + 1
                res = mid
            if mid * mid > x:
                end = mid -1
        return res        
