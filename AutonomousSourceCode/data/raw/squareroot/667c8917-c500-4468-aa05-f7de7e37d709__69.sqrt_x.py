# Implement int sqrt(int x).

# Compute and return the square root of x.

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        i, j = 0, x / 2 + 1
        while i <= j:
            mid = (i + j) / 2
            cur = mid ** 2
            if cur == x:
                return mid
            elif cur < x:
                i = mid + 1
            else:
                j = mid - 1

        return (i + j) / 2
