import math
import sys
def strict_floor(f):
    if int(math.floor(f)) == f:
        return int(f - 1)
    else: 
        return int(math.floor(f))
    
def strict_ceil(f):
    if int(math.ceil(f)) == f:
        return int(f + 1)
    else:
        return int(math.ceil(f))

def is_square(n):
    root = int(math.sqrt(n))
    if root*root == n:
        return True
    else:
        return False

def count_square_quads(m):
    n_with_square = 0
    primes = [1,2,3,5,7,11,13,17,19,23,29,
              31,37,41,43,47,53,59,61,67,71,
              73,79,83,89,97]
    been_counted = {}
    for i in range(1,m+1):
        for j in range(1,m+1):
            for k in range(1,m+1):
                for l in range(1,m+1):
                    been_counted[i + j*(10**3) + k*(10**6) + l*(10**9)] = False

    for a in range(1,m+1):
        if m==100: print "a = ", a
        for b in range(1,m+1):
            for c in range(1,m+1):
                for d in range(1,m+1):
                    if been_counted[a + b*(10**3) + c*(10**6) + d*(10**9)] == True: continue
                    n_pts = 0
                    for x in range(-c+1,0):
                        low = strict_ceil( -(d/float(c))*x -d )
                        high = strict_floor( (b/float(c))*x + b ) + 1
                        #print "1: x: ",x
                        #print "1: high, low: ", high, low
                        #print "1: inputs: ", -(d/float(c))*x -d , (b/float(c))*x + b 
                        for y in range(low,high):
                            n_pts +=1
                    for x in range(0,a):
                        low = strict_ceil( (d/float(a))*x -d )
                        high = strict_floor( -(b/float(a))*x + b ) + 1
                        for y in range(low,high):
                                n_pts += 1
                    if is_square(n_pts): 
                        n_with_square += 1
                        been_counted[a + b*(10**3) + c*(10**6) + d*(10**9)] == True
                        #print "values: ", a, b, c, d
                        #print "max int: ", sys.maxint
                        #check all symmetry solutions
                        #flip a->c
                        if a!=c and been_counted[c + b*(10**3) + a*(10**6) + d*(10**9)] == False:
                            n_with_square+=1
                            been_counted[c + b*(10**3) + a*(10**6) + d*(10**9)] =True
                        #flip b->d
                        if b!=d and been_counted[a + d*(10**3) + c*(10**6) + b*(10**9)] == False:
                            n_with_square+=1
                            been_counted[a + d*(10**3) + c*(10**6) + b*(10**9)] =True     
                        #flip both
                        if a!=c and b!=d and been_counted[c + d*(10**3) + a*(10**6) + b*(10**9)] == False:
                            n_with_square+=1
                            been_counted[c + d*(10**3) + a*(10**6) + b*(10**9)] =True
                        #permutes
                        if a!=b and b!=c and c!=d and d!=a and a!=c and b!=d:
                            #permute 1
                            if been_counted[b + c*(10**3) + d*(10**6) + a*(10**9)] == False:
                                n_with_square+=1
                                been_counted[b + c*(10**3) + d*(10**6) + a*(10**9)] =True
                            #permute 2
                            if been_counted[c + d*(10**3) + a*(10**6) + b*(10**9)] == False:
                                n_with_square+=1
                                been_counted[c + d*(10**3) + a*(10**6) + b*(10**9)] =True
                            #permute 3
                            if been_counted[d + a*(10**3) + b*(10**6) + c*(10**9)] == False:
                                n_with_square+=1
                                been_counted[d + a*(10**3) + b*(10**6) + c*(10**9)] =True
                                    
    print "number of squares for m = ", m, "is", n_with_square

count_square_quads(1)
count_square_quads(2)
count_square_quads(3)
count_square_quads(4)
count_square_quads(5)
count_square_quads(6)
count_square_quads(7)
count_square_quads(8)
count_square_quads(9)
count_square_quads(10)
count_square_quads(50)
