import math
from pyspeedup.algorithms import jacobi_symbol

def powersInMod(n):
    ''' Computes all the squares in the integers mod n.
    '''
    return set((x*x)%n for x in range(0,n//2+1))

def isSquare(n):
    '''Checks for perfect squares by checking mod 64 to rule out 52/64 cases immediately.'''
    if n%isSquare.mod in isSquare.set:
        m=math.floor(math.sqrt(n))
        return m*m==n
    return False
isSquare.mod=64 #This can be changed if a different value is deemed better.
isSquare.set=powersInMod(isSquare.mod) #The set of all perfect squares mod the above number.

def tsSquareRoot(a,p): #Currently requires p to be prime.
    '''Calculates the square root mod p of a.'''
    jacobi=jacobi_symbol(a,p)
    if jacobi==-1:
        raise ValueError("No square root mod {0} exists.".format(p))
    s=p-1
    e=0
    while s%2==0: #Find p-1=s*2^e with odd s.
        e+=1
        s//=2
    n=findQuadraticNonresidue(p)
    x=pow(a,((s+1)/2),p) #first guess
    b=pow(a,s,p) #first guess correction
    g=pow(n,s,p) #quantity to modify x and b
    r=e
    while r>0:
        #ord_p(g)=ord_p(pow(n,s,p))
        #Note (n^s)^2^e=n^(2^e*s)=n^(p-1)=1 mod p
        #claim ord_p(g)=2^e, because
        #(n^s)^2^(e-1)=n^(s*2^e)/2=n^((p-1)/2)=jacobi_symbol=-1
        #Find m s.t. 0<=m<r and b^(2^m)==1
        m=0
        bp=b
        while m<r:
            if bp==1:
                break
            bp=(bp*bp)%p
            m+=1
        if m==0:
            break
        #Having found m, we update:
        g=pow(g,pow(2,(r-m-1),p),p)
        x=(x*g)%p
        g=(g*g)%p
        b=(b*g)%p
        r=m
    return x

def findQuadraticNonresidue(p):
    if p%8 in [3,5]:
        return 2
    elif p%8==7:
        return p-2
    n=2
    while jacobi_symbol(n,p)!=-1:
        n+=1 #Find an n s.t. (n/p)==-1
    return n