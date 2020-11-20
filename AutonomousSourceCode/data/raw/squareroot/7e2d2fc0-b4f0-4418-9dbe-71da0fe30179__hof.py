#!/usr/bin/python

def square_root(x):
	def update(guess):
		return average(guess,x/guess)
	def test(guess):
		return approx_eq(square(guess),x)
	return iter_improve(update,test)

def approx_eq(x,y,tol=1e-5):
	return abs(x-y) < tol

def square(x):
	return x*x

def average(x,y):
	return (x+y)/2

def iter_improve(update,test,guess=1):
	while not test(guess):
		guess = update(guess)
	return(guess)

#def sqrt_update(guess,x):
#	return average(guess,x/guess) 
