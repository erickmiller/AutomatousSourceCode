import math


def square_root_method(a,x):
    while True:
        #print x 
        y=(x+a/x)/2
        if y==x:
            break
        x=y
    return y
    
print(square_root_method(9,8))
print(type(square_root_method(9,10)))
        
        
def table():
    for i in range(1,10):
        tabelle=[]
        p=math.sqrt(i)
        #print(p)
        q=square_root_method(i,i+1)
        #print(q)
        r=abs(p-q)
        #print(r)
        tabelle.append([i, p, q, r])
        print(tabelle)
    return tabelle

print tabulate(table())


    