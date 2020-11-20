import math
import time

t1 = time.time()

# a,b,c

# c >= b >= a
# l >= root(3)*a
# a+b > c

# b2 = p2+q2-2pq*(-1/2) = p2+q2+pq
# a2 = q2+r2-2qr*(-1/2) = q2+r2+qr
# c2 = p2+r2-2pr*(-1/2) = p2+r2+pr

def isSquare(n):
    r = math.sqrt(n)
    if r == int(r):
        return int(r)
    return 0

# p >= q >= r

N = 120000

rset = []
for r in range(3,N//3+1):
    for q in range(r,(N-r)//2+1):
        a = isSquare(q*q+r*r+q*r)
        if a > 0:
            for p in range(q,N-r-q+1):
                b = isSquare(p*p+q*q+p*q)
                if b > 0:
                    c = isSquare(p*p+r*r+p*r)
                    l = p+q+r
                    if c > 0 and not l in rset:
                        rset.append(l)
                        #print(a,b,c,p,q,r,l)

print(sum(rset))

      
print("time:",time.time()-t1)  
# time: 6303.283174037933

    
