"""
Implement int sqrt(int x).
Compute and return the square root of x.
Problem found here:
http://oj.leetcode.com/problems/sqrtx/
"""

import math

"""
A fairly basic solution which implements the Babylonian method.
I have added in a few options to allow some control over the accuracy
and speed.
"""
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x, blind_steps=0, accepted_error=1):
        if x < 0:
            print 'error, cannot compute square root of negative number'
            return -1
        if x == 0:
            return x
        root = x/2.0
        steps = -1
        while True:
            root = 0.5 * (root + x/root)
            steps += 1
            if steps >= blind_steps:
                steps = 0 
                if (root * root) - x < accepted_error:
                    return int(root)



#test
sol = Solution()
values = [25, 125, 1, 1234225]
for i in values:
    print 'for the value', i,
    print 'the actual square root is', math.sqrt(i)
    print 'the integer square root we find is', sol.sqrt(i)
    print '---'
