from math import *

def square_root(a):
	x = a/2.0
	while True:
		y = (x + a/x) / 2.0
		if abs(y-x) < 0.000000001:
			break
		x = y
	return y

"""
To test the square root algorithm in this chapter, you could compare
it with math.sqrt. Write a function named test_square_root that prints
a table like this:

1.0 1.0           1.0           0.0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
"""
def test_square_root(a):
	for i in range(1,a+1):
		sr1 = square_root(i)
		sr2 = sqrt(i)
		print("{0}  {1:<15}{2:<15}{3}".format(i, sr1, sr2, abs(sr1-sr2)))


"""
Write a function called eval_loop that iteratively prompts the
user, takes the resulting input and evaluates it using eval,
and prints the result.
It should continue until the user enters 'done', and then return
the value of the last expression it evaluated.
"""
def eval_loop():
	print("enter expression to evaluate. 'done' to stop")
	evaluated_exp = None
	while True:
		exp = input(">>> ")
		if exp == "done":
			break
		evaluated_exp = eval(exp)
		print(evaluated_exp)
	return evaluated_exp


"""
The mathematician Srinivasa Ramanujan found an infinite series that
can be used to generate a numerical approximation of π
Write a function called estimate_pi that uses this formula to compute
and return an estimate of π. It should use a while loop to compute
terms of the summation until the last term is smaller than 1e-15
(which is Python notation for 10−15).
"""
def factorial(n):
    """Computes factorial of n."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def estimate_pi():
	factor = (2 * square_root(2) / 9801)
	total = 0
	k = 0
	while True:
		ex1 = factorial(4*k) * (1103+26390*k)
		ex2 = factorial(k)**4 * (396**(4*k))
		term = factor * ex1 / ex2
		total += term
		if abs(term) < 1e-15:
			break
		k += 1

	return 1 / total
