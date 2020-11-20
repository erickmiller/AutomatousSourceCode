"""
olve the equation x2+4x+1=0 in Z23. Use the method described in lecture 9.3 using the quadratic formula.

############
Solution:

- see page 26

"""

def egcd(x, y):
    a,b, u,v = 0,1, 1,0
    while x != 0:
        q, r = y//x, y%x
        m, n = a-u*q, b-v*q
        y,x, a,b, u,v = x,r, u,v, m,n
    return y, a, b

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

a = 1 
b = 4
c = 1
p = 23

# Find (2a)^(-1) in Z_p using extended Euclid
inv = modinv(2*a, p)

# Find square root of b^2-4*a*c in Z_p using a square root algorithm
# p = 23  ---> 23 mod 4 = 3 mod 4, so we could use sqr(c) = c^((p+1)/4) in Z_p
sqr_term = pow(b,2) - 4 * a * c
root = pow(sqr_term, (p+1)/4)

x1 = ((-b + root) * inv) % p
x2 = ((-b - root) * inv) % p

print "x1 =", x1
print "x2 =", x2



 
