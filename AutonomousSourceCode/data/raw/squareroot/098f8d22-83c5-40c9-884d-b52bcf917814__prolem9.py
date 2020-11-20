__author__ = 'Shivaji'
import math

def squareroot(a,b):
    a1=a*a
    b1=b*b
    c=a1+b1
    result=math.sqrt(c)
    print("Result of square root of a %d and b %d is %c",a,b,result)
    if result.is_integer()==False:
        return 0
    else:
        return result


a=3
b=4
c=5
sum=0
n=2

while(True):
    result=squareroot(a,b) #square root of a square + b square
    if result:
        c=result
        sum=a+b+c
        if sum>=1000:
            print("a:%n b: %n c: %n sum is",a,b,c,math.pow(a,2)+math.pow(b,2),math.pow(c,2),sum)
            break
        else:
            a=3*n
            b=4*n
            n=n+1

a1=3*n-1