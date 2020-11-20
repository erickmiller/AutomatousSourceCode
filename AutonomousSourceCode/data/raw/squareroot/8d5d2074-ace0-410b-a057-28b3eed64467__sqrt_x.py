"""
Implement int sqrt(int x).

Compute and return the square root of x.

"""

def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    # the root of x will not bigger than x/2 + 1
    if x == 0:
        return 0
    elif x == 1:
        return 1
    l = 0
    r = x/2 + 1
    while r >= l:
        mid = (r + l) /2
        temp = x / mid
        if temp == mid:
            return mid
        elif temp < mid:
            r = mid - 1
        else:
            l = mid + 1
    return r
