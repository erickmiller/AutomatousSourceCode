"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""


class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x <= 1:
            return x
        lo, hi = 0, 1 + x / 2
        while lo + 1 < hi:
            mid = lo + (hi - lo) / 2
            square = mid ** 2
            if square == x:
                return mid
            elif square < x:
                lo = mid
            else:
                hi = mid
        return lo


if __name__ == '__main__':
    s = Solution()
    print s.mySqrt(2)
