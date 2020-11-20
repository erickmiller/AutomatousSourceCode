# -*- coding: utf-8 -*-
"""
Implement int sqrt(int x).

Compute and return the square root of x.

@author: weichen
"""
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x < 0: return -1
        if x == 0: return 0
            
        s = 1; e = x/2 + 1    
        
        while s <= e:
            m = (s + e)/2
            if m*m <= x and (m+1)*(m+1) > x:
                return m
            elif m*m < x:
                s = m + 1
            else:
                e = m - 1
        return 0
    
#    USE Newton's method, works also for float!!!!!!!!!!
    def sqrt2(self, x):
        if x < 0: return -1
        if x == 0: return 0

        lasty = 0
        y = x/2.
        while abs(lasty - y) > 1e-3:
            lasty = y
            y = (y + x/y)/2
            
        return int(y)


        
if __name__ == "__main__":
    test = Solution()
    l = [2,4,8,9,10]
    for i in l:
        print "the sqrt root of", i, "is", test.sqrt2(i)
            