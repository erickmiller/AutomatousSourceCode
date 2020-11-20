"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""
#O(n)
def sqrt1(x):
    i = 0
    while i*i != x:
        i = i+1
    return i

def sqrt(x):
    l = 0
    h = x
    while l<=h:
        m = l + h/2
        if m*m == x:
            return m
        elif m*m <x:
            l = m+1
        else:
            h= m-1
    return (l+h)/2
print sqrt(9)