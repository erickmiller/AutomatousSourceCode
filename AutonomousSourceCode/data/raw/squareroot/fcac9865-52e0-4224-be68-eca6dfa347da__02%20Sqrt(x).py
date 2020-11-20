# Sqrt(x)
# Implement int sqrt(int x).
# Compute and return the square root of x.
#
# Example
# sqrt(3) = 1, sqrt(4) = 2, sqrt(5) = 2
#
#Challenge
# O(log(x))

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x < 0: return None
        if x == 0: return 0
        
        start, end = 1, x
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid ** 2 > x:
                end = mid
            else:
                start = mid
            
        if end ** 2 <= x:
            return end
        return start
                
