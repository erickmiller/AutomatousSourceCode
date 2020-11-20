import math
import time

t1 = time.time()

# use [num,a,b,c] to store a/b*(sqrt(num)-c)
def valueOf(com):
    result = (math.sqrt(com[0])-com[3])*com[1]/com[2]
    return math.floor(result*math.pow(10,6))

def gcd(x,y):
    if x < y:
        temp = x
        x = y
        y = temp
    while y > 0:
        temp = x%y
        x = y
        y = temp

    return x

def oneOver(com):
    na = com[2]
    nb = com[1]*(com[0]-com[3]*com[3])
    nc = -com[3]
    d = gcd(na,nb)
    return [com[0],na//d,nb//d,nc]

def head(com):
    return int(valueOf(com)//math.pow(10,6))

def trun(com,a):
    nc = com[3]+a*com[2]/com[1]
    return [com[0],com[1],com[2],nc]
    
def notation(num):
    root = math.sqrt(num)
    a = math.floor(root)
    if a == root:
        return [a,[]]
    rest = [num,1,1,a]
    mark = valueOf(rest)
    lst = []
    while True:
        temp = oneOver(rest)
        na = head(temp)
        lst.append(na)
        rest = trun(temp,na)
        if valueOf(rest) == mark:
            break
    return [a,lst]
        
def period(note):
    return len(note[1])

def digseq(num,i):
    note = notation(num)
    if i == 0:
        return note[0]
    p = period(note)
    return note[1][(i-1)%p]

def convergent(num,n):
    if n == 1:
        return [notation(num)[0],1]
    i = n-1
    temp = [1,digseq(num,i)]
    while True:
        i -= 1
        t = digseq(num,i)
        ntemp = [t*temp[1]+temp[0],temp[1]]
        if i == 0:
            return ntemp
        flip = [ntemp[1],ntemp[0]]
        temp = flip[:]

# wikipedia pell's equation

def Dmim(d):
    i = 0
    while True:
        i += 1
        ab = convergent(d,i)
        x = ab[0]
        y = ab[1]
        if x*x-d*y*y == 1:
            return x

def square(num):
    root = math.sqrt(num)
    r = math.floor(root)
    if r == root:
        return True
    return False

largest = 0
td = 0
for i in range(2,1001):
    if not square(i):
        md = Dmim(i)
        if md > largest:
            largest = md
            td = i

print(td)


print("time:",time.time()-t1)
