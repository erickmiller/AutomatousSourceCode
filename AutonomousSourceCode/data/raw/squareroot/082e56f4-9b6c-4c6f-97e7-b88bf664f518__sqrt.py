"""
An algorithm for finding the square root of an integer, x

Start by initializing s as a guess. 
If we take the average of s + x/s for enough iterations, we will
always converge on the square root.

Why: If our guess, s, is too small, x/s will be larger than the true square root
	 If our guess, s, is too large, x/s will be smaller than the true squeare root
	 If it's just right, x/s will be the square root.

Therefore, continuous average iterations will hone in on the true square root!

Enhancements: max_iteration and tolerance -- cap the iterations, but check the delta of s at each 
			  iteration and break from the loop if delta is less than our tolerance level.


"""

def sqrt(number, guess, max_iterations=200, tolerance=1.e-14):
	
	s = guess

	for k in range(max_iterations):
		print ("Before iteration: %s, s = %20.15f" % (k, s))
		s0 = s
		s = 0.5 * (s + number/s)
		delta_s = s - s0
		if abs(delta_s / number) < tolerance:
			break
	print ("After %s iterations, s = %20.15f" % (k+1, s))
	return s 



if __name__ == "__main__":
	sqrt(16, 1)
