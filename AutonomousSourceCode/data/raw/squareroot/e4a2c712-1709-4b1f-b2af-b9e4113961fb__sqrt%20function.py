#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cain297
#
# Created:     27/03/2012
# Copyright:   (c) cain297 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()
x = int(raw_input("Please enter a non-negative integer"))

def sqrt(x):
    #Returns the Square Root of the value input
    i= 0
    if x >= 0:
        while i < x:
            if i*i == x:
                print i, "is the square root of the number", x
                return None
            elif i*i >x:
#                print "I am here"
                print x, "is not a perfect square"
                return None
            else:
                i += 1


    else:
        print x + "is not a positive integer"
        return None

sqrt(x)
