import math
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
    for a in range(1,m+1):
        if m==100: print "a = ", a
        for b in range(1,m+1):
            for c in range(1,m+1):
                for d in range(1,m+1):
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
                    if is_square(n_pts): n_with_square += 1
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
count_square_quads(11)
count_square_quads(12)
count_square_quads(13)
count_square_quads(14)
count_square_quads(15)
