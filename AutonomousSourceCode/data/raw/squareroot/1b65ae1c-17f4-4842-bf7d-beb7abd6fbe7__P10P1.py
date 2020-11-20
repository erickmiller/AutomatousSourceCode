__Author__ = "Conor O'Kelly"


"""
Pseudocode

Get input
    Convert input to int

Test if input negative
    If negative quit
    If positive continue

While input is not equal to (integer ** 2 ) or count
    count += 1

    if (integer ** 2) == input
        Square root found
    if input == count
        square root not found

"""

# squre root finder function

def square_root():

    number = get_input_int()

    if number > 0:
        find_square(number)
    else:
        print "The number entered is below 0. Program quiting."

# Find square root

def find_square(number):

    result = 0
    count = 0
    
    # Test exhaustive enumberation
    while number != result and number != count:

        # Order is important. Need to increase count. Then generate result for testing
        count += 1
        result = count ** 2
            
    # Print correct statements
    if number == result:
        print "The square root of %i is %i" % (number, count)
    else:
        print "Could not find the square root for the number %i" % (number)

    

# Get input and convert to in function

def get_input_int():

    number = raw_input ("Please give me a number \n")
    number = int(number)

    return number

# Test 1
square_root()
