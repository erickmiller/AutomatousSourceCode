import primes
import math

def minimal_solution(D):
    # Find smallest integer whose square > D.
    root = int(math.sqrt(D)) + 1
    while True:
        left = root*root-1
        if left % D == 0:
            if primes.is_square(left/D):
                return root 
        root += 1

def solve66(max_D):
    largest = 0
    for D in range(max_D):
        if not primes.is_square(D):
            min_solution = minimal_solution(D)
            if min_solution > largest:
                print min_solution
                largest = min_solution
    return largest

print "finished! " + str(solve66(1001))
        
