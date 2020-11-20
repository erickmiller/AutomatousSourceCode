import math
import time

def solution(A):
	start = time.time()

	length = len(A)
	A_sort = sorted(A)
	#print(A_sort)
	gaps = []

	#print "range of y: " + str(range(min(A_sort), max(A_sort)))
	#print "sorted array: " + str(A_sort)

	for y in range(min(A_sort), max(A_sort)):
		gaps_for_y = []

		for i in range(0,length):
			gaps_for_y.append(abs(y - A_sort[i]))

		gaps.append(min(gaps_for_y))

	solution = max(gaps)
	#print solution

	end = time.time()

	runtime = end-start

	return float(runtime)

	#print "Time Elapsed:	" + time



