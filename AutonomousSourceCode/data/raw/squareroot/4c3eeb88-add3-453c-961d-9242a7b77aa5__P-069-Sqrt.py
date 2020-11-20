'''
P-069 - Sqrt(x)

Implementint sqrt(int x). Compute and return the square root ofx.

Tags: Math, Binary Search
'''

class Solution:
    # @param x, an integer
    # @return an integer
    def binary_search(self, x, y):
        m = (x + y) / 2
        if x > y:
            return y 
        if m * m > self.target:
            return self.binary_search(x, m - 1)
        elif m * m < self.target:
            return self.binary_search(m + 1, y)
        else:
            return m

    def sqrt(self, x):
        self.target = x
        return self.binary_search(0, x)

s = Solution()

print s.sqrt(100)