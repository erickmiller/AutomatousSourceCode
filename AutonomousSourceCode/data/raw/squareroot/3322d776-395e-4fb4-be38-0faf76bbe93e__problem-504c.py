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

def count_in_right_triangle(s1,s2):
    n_in = 0
    for x in range(1,s1):
        #high = int(math.floor( -(s2/float(s1))*x + s2 )) + 1
        #print "argument: ", -(s2/float(s1))*x + s2
        #print "floor: ", high - 1
        for y in range(1,s2):
            if s1*y < -s2*x + s2*s1 :
                n_in += 1
    return n_in

print "in 3,9 triangle:", count_in_right_triangle(3,9)
print "in 1,100 triangle:", count_in_right_triangle(1,100)
def count_on_cross(a,b,c,d):
    counts =  a + b + c + d -3
    return counts

def count_square_quads(m):

    #pre-generate pairwise triangle counts
    triangle_count = {}
    for i in range(1,m+1):
        for j in range(1,m+1):
            triangle_count[i + j*(10**4)] = count_in_right_triangle(i,j)
    #print triangle_count[100 + 100*(10**4)]
    #print "triangle count: ", count_in_right_triangle(100,100)
    n_with_square = 0
    for a in range(1,m+1):
        if m==100: print "a = ", a
        for b in range(1,m+1):
            for c in range(1,m+1):
                for d in range(1,m+1):
                    n_pts = (count_on_cross(a,b,c,d) +
                             triangle_count[a+b*(10**4)] +
                             triangle_count[a+d*(10**4)] + 
                             triangle_count[d+c*(10**4)] + 
                             triangle_count[b+c*(10**4)])
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
count_square_quads(100)
