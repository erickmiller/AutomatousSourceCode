# File Name: newton.py
# Using newton's algorithmn, compute the square root of the input
# and error
#
# Helen Chac, ECS 010, FALL 2012
#

# import math functions
import math

def newton(k):

    # raise error if inputted number is negative
   if k<0:
        raise ValueError("Cannot take the square root of a negative number")
   else:
        x = k/2 #take half of the guess
            
        # repeat until the difference of the guess is 10 ** (-10) 
        while abs (k - x**2) >= ((10) ** (-10)):

            # assign x to plus x and k / x and divide by 2 
            x = (x + k / x ) / 2
            
        # return the value x 
        return x

def main():

    # use try to catch errors
    try:
        k = float (input ("Number? "))

            # the x from newton (k)
        x = newton(k)
            
            # compute the error for the print
        error = abs ( math.sqrt(k) - x )

            # print square root
        print ("The approximate square root of", k, "is", "%.10f" % x)

            # print error
        print ("The error is", error )

    # if text is printed in the input, it will print
    # "cannot take the square root of a negative number"
    except ValueError as msg:
        print (msg)

    # stop program if user types in control + D        
    except EOFError as msg:
        print (" ")
        
# run main
main()
