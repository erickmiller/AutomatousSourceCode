"""
Unit 1 - Lecture 1
Find a square root
author: Chris Lee
created: 10/14/2013
"""

def sqrt(number, guess = 1):
	if abs(number - guess*guess) < 5*pow(10,-(dec_accuracy + 1)):
		return guess
	else:
		return sqrt(number, guess = (float(number/guess) + guess)/2)

if __name__ == "__main__":
	dec_accuracy = 5
	square = 38
	print "The square root of %s is %s" % (square, sqrt(square))
	print "It is %f from the actual square-root" % (abs(pow(square,.5) - sqrt(square)))
