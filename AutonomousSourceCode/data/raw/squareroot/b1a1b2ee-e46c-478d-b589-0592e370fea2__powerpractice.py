'''square,cube,root,and power.

Available functions:

square(number)
    returns the square of a number

cube(number)
    returns the cube of a number

root(number)
    returns the square root of a number

power(number, power)
    returns then number to the power'th power

Example Usage:
>>> import powerpractice
>>> powerpractice.square(2)
4
>>> powerpractice.cube(2)
8
>>> powerpractice.root(9)
3
>>> powerpractice.power(9,0.5)
3
>>> powerpractice.power(3,2)
9

'''

def square(number=1):
    '''Return the square of the number.'''
    return number * number

def root(number=1):
    '''Return the square root of the number.'''
    return number ** 0.5

def cube(number=1):
    '''Return the cube of the number.'''
    return number * number * number

def power(number=1,power=1):
    '''Return the number raised to the power.'''
    return number ** power

if __name__ == '__main__':
    print( 'square of 2' )
    print( square(2) )
    print( 'cube of 2' )
    print( cube(2) )
    print( '2 to the power of 16')
    print( power(2,16) )
    print( '81 to the power of 0.5')
    print( power(81,0.5) )
    print( 'square root of 81')
    print( root(81) )
