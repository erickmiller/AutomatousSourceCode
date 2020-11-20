#finds the first triangle number with more than x numbers of factors

def findFactors(n):
    x=[]
    #creates an array
    z=n
    x.append(z)
    x.append(1)
    y=z**.5+1
    p=2
    #makes a variable that is one more than the square root of z
    while p<y:
        #continues until y is 1
        if z%p==0:
            #if y is a factor of z it adds it and its opposite to the array
            x.append(p)
            x.append(z/p)
            p=p+1
        else:
            p=p+1
    x.sort()
    
    return x

def main():
    x=1
    i=2
    while len(findFactors(x))<500:
        x=x+i
        i=i+1
    print x
main()
