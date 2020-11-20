#shortest path is always diagonal created by two shorter sides added together and longest side
#in a right triangle
#shortest path is integer if hypotenuse is a square


def is_square(n):
    root = float(n) ** .5
    root = int(root+.5)
    if root*root == n:
        return root
    else:
        return False
        
M = 10000
count = 0
#test function doing it naive way, used to verify next function on small values
for x in range(1,M+1):
    break
    for y in range(1,x+1):
        for z in range(1,y+1):
            if(is_square(x*x + (y+z)*(y+z))):
                count +=1
#print count
count  = 0


#for each possible sum of the shorter two sides I find the number of ways the sides can add up to that                
for x in range(1,M+1):
    for yz in range(2,2*x+1):
        if(is_square(x*x + yz*yz)):
            if yz <= x+1:
                count += yz/2
            else:
                count += yz/2 - (yz - x-1)
    if count > 1000000:
        print "M val", x
        break
print count
            
