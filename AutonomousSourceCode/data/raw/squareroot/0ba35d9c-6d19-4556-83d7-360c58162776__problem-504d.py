import math

def is_square(n):
    root = int(math.sqrt(n))
    if root*root == n:
        return True
    else:
        return False


def count_side(a,b):
    n_pt = 0
    
    for x in range(0,a+1):
        for y in range(0,b+1):
            if y*a  == -b*x + a*b:
                n_pt+=1
    return n_pt


def calc_twice_area(a,b,c,d):
    area = 0
    area += a*b
    area += a*d
    area += d*c
    area += b*c

    return area

def count_square_quads(m):
    boundary = {}
    for i in range(1,m+1):
        for j in range(1,m+1):
            boundary[i + j*(10**4)] = count_side(i,j)

    n_with_square = 0
    for a in range(1,m+1):
        if m==100: print "a = ", a
        for b in range(1,m+1):
            for c in range(1,m+1):
                for d in range(1,m+1):
                    tot_boundary = (boundary[a+b*(10**4)] + 
                                    boundary[a+d*(10**4)] + 
                                    boundary[d+c*(10**4)] + 
                                    boundary[b+c*(10**4)] )
                    tot_boundary-=4
                    n_pts = int(calc_twice_area(a,b,c,d) - tot_boundary + 2)
                    n_pts /= 2
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
