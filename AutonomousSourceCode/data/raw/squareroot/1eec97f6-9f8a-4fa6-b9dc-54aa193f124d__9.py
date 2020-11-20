import math

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False



for i in range(1,1001):
    for j in range(1,1001):
        ab = i**2 + j**2
        c = math.sqrt(ab)
        if is_square(ab) == True and i > j and (i + j) == 1000 - c:
            print(i,j,c)
            print(i*j*c)
            print(i+j+c)
        
  
