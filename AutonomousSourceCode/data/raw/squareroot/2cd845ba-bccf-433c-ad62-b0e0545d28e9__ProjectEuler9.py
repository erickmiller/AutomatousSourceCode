__author__ = 'matt'
import math
def isWholeNumber(x,y):
    val = x**2 + y**2
    if is_square(val):
        return True
    return False
def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False
found = False
for x in range (1, 1000):
    for y in range(1,1000):
        if isWholeNumber(x,y):
            val = math.sqrt(x**2+y**2)
            sum = x + y + val
            if(int(sum) == 1000):
                print x
                print y
                print val
                found = True
                break
    if(found):
        break
print (200*375*425)
