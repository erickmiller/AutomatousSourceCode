import math
def square_root(a):
    x=a+0.01
    while True:
        epsilon=0.000000000001
        y=(x+a/x)/2
        if abs(y-x)<epsilon:
            return y
            break
        x=y

def test_square_root(n):
    for k in range(1,n+1):
        x=square_root(k)
        y=math.sqrt(k)
        z=abs(x-y)
        print(k,x,y,z)

def estimate_pi():
    k=0
    s=0
    a=2*math.sqrt(2)*1103/9801
    while a>1e-15:
        s+=a
        k+=1
        a=(2*math.sqrt(2)*math.factorial(4*k)*(1103+26390*k))/(9801*(math.factorial(k)**4)*(396**(4*k)))
    return 1/s

def bisection(l,a,k):
    if l[math.floor(len(l)/2):][0]<a:
        print(k)
        k=k+math.floor(len(l)/2)
        print(k)
        bisection(l[math.floor(len(l)/2):],a,k)
    elif l[math.floor(len(l)/2):][0]==a:
        return k+1
    else:
        bisection(l[:math.ceil(len(l)/2)],a,k)
testlijst=list(range(1, 9))
bisection(testlijst,7,0)