'''

Implement int sqrt(int x).

Compute and return the square root of x.

Created on Jan 12, 2014

@author: Songfan
'''

''' thought: binary search from 0 to x and judge if the current val square is greater or less than x '''

def sqrt(x):
    assert(x > 0), 'input error'
    if x < 2: return x
    
    first = 0
    last = x // 2
    ''' caveat: 'last' is init to be x/2, while(first <= last) '''
    while(first <= last):
        mid = (first + last) // 2
        val = mid * mid
        if val == x: return mid
        elif val < x: first = mid + 1
        else: last = mid - 1
    return mid

x = 80
print sqrt(x)