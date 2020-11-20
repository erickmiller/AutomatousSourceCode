'''
Step by step to crack Programming Interview questions 2. 
Get square root of a number using binary search.
'''



def getSquareRoot_Wrapper(target, precision):
    return getSquareRoot_recur(0, target, target, precision)

#assume num is positive
def getSquareRoot_recur(left, right, target, precision):
    print("called")
    candidate = (left+right)/2
    
    if(target-candidate**2==0 or abs(target-candidate**2)<precision):
        return candidate
    elif(candidate**2>target):
        left = left
        right = candidate
        candidate = getSquareRoot_recur(left, right, target, precision)
        return candidate
    else:#(candidate**2 < target):
        left= candidate
        right = right
        candidate = getSquareRoot_recur(left, right, target, precision)    
        return candidate
        
print(getSquareRoot_Wrapper(100, 0.000001))

    
