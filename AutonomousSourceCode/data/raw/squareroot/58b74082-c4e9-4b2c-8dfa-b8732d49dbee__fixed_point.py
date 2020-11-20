# Name: Dylan Jones
# Date: 24/1/2013
# File: fixed_point

import math

#global variable for the range of tolerance
tolerance_range = 0.000000001

def average( x, y ) :
  return ( x + y ) / 2.0

def average_damp( function ) :
  return lambda x : average( x, function( x ) )

#return if the tolerance range has been meet
def is_small_enough(neg_point, pos_point) :
  tolerance = abs(neg_point - pos_point) / 2.0
  return tolerance <= tolerance_range

def find_fixed_point( function, guess ) :
  next_guess = function( guess )
  if is_small_enough( guess, next_guess ) :
    return next_guess
  else :
    return find_fixed_point( function, next_guess )

def square_root( n ) :
  return find_fixed_point(lambda x: average( x, n / x), 1)

def cubic_root(n):
  return find_fixed_point( average_damp ( lambda x: n / ( x * x ) ), 1)

def golden_ratio():
  return find_fixed_point( lambda x: average( x, ( x + 1 ) / x ), 1 ) 

square_root_2 = square_root( 2 )
square_root_3 = square_root( 3 )
square_root_9 = square_root( 9 )

cubic_root_2 = cubic_root( 2 )
cubic_root_3 = cubic_root( 3 )
cubic_root_9 = cubic_root( 9 )

golden_ratio = golden_ratio()

print "square_root_2 : " + str( square_root_2 ) + "\n"
print "square_root_3 : " + str( square_root_3 ) + "\n"
print "square_root_9 : " + str( square_root_9 ) + "\n"
print "cubic_root_2 : " + str( cubic_root_2 ) + "\n"
print "cubic_root_3 : " + str( cubic_root_3 ) + "\n"
print "cubic_root_9 : " + str( cubic_root_9 ) + "\n"
print "golden_ratio : " + str( golden_ratio ) + "\n"

