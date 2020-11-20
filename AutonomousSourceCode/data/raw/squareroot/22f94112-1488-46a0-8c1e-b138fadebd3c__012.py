#!/usr/bin/python
from math import sqrt
'''
    Purpose: https://projecteuler.net/problem=12
    A direct brute force approach
    @author:Pramod S   
'''
def numberofDivisors(num):
    nod,squareRoot=0,int(sqrt(num))
    for i in range(1,squareRoot+1):
        if(num%i==0):
            nod+=2
    if((squareRoot*squareRoot) == num):
        nod = nod - 1
    return nod
    
def main():
    number,i=0,1
    while(numberofDivisors(number) < 500):
        number+=i
        i+=1
    print("Result: {0}".format(number))
if __name__ == "__main__":
    main()
