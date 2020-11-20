
def sequence(n):
    while n != 1:
        print n
        if n%2 == 0:
            n = n/2
        else:
            n = n*3+1

#print sequence(3)



#練習問題7.1
def print_n(s, n):
    while n <= 0:
        return
    print s
    print_n(s, n-1)
    
print_n("Hello",5)

#練習問題7.2  
def square_root(a):
    x = a / 2.0
    epsilon = 0.000000000001
    while True:
        y = (x + a/x) / 2.0
        if abs(y-x) < epsilon:
            break
        x = y
    return x
    
print square_root(49)
