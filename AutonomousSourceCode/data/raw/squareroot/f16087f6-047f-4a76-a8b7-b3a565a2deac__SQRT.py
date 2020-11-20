__author__ = 'Vivek'
#Find Square root of an inetger , if Square root is not integer returns floor of sqrt
def sqrt(A) :
        if 2 > A :
            return A
        low = 0
        high = A
        while high > low + 1 :
            num = (low + high)/2
            if num**2 < A  :
                low = num
            elif num**2 > A :
                high = num
            else :
                break
        if A == num**2:
            return num
        else :
            return low

print(sqrt(25))
