#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-04-29 23:57:23
# Title      :  69 sqrtx

# Implement int sqrt(int x).
#
# Compute and return the square root of x.

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        def isGood(val):
            return abs(val * val - x) / x < 0.00001
            
        def improve(val):
            return (val + x / val) / 2
            
        def iter(val):
            if isGood(val):
                return val
            else:
                return iter(improve(val))
        if x == 0 or x == 1:
            return x
        
        result = int(iter(1.0))
        if result * result > x:
            return result - 1
        return result
