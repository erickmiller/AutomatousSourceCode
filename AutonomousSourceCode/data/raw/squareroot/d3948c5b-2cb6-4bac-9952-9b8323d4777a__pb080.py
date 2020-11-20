import math
import time

t1 = time.time()

def square(lst):
    n = len(lst)
    temp = [0]*(n*2-1)
    for i in range(0,n):
        for j in range(0,n):
            temp[i+j] += lst[i]*lst[j]
    for i in range(0,len(temp)-1):
        if temp[-1-i] > 9:
            temp[-2-i] += temp[-1-i]//10
            temp[-1-i] = temp[-1-i]%10
    return temp

def bigger(num,lst):
    if lst[0] >= num:
        return False
    return True
    
def root(num):
    x = 100
    temp =[math.floor(math.sqrt(num))]
    while len(temp) < x:
        temp.append(1)
        while temp[-1] < 10 and bigger(num,square(temp)):
            temp[-1] += 1
        temp[-1] -= 1
    return temp

def isSquare(num):
    r = math.floor(math.sqrt(num))
    if r*r-num == 0:
        return True
    return False

total = 0
for i in range(2,100):
    if not isSquare(i):
        n = sum(root(i))
        total += n

print(total)

print("time:",time.time()-t1)
    
