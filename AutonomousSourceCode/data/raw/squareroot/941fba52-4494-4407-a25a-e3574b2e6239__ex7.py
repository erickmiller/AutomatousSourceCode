import math

#ex 7.1 rewrite a recursive function from ch 5 as a while loop
def print_n(s,n):
    while n > 0:
        print(s),
        n = n - 1

print_n('bok choy', 5)
print_n('boobs', 2)
print_n('palm trees are great!', 8)



#7.4 break example
while True:
    line = input('> ')
    if line == 'done':
        break
    print (line)

print('Done!')

#example 7.6 of newtons squareroot approximation algorithm
#ex7.2
def sqrt2(a):
    x = a/4
    while True:
        y = (x+a/x)/2
        if x == y:  
            return x
        x = y

print(sqrt2(4))
print(sqrt2(144))
print(sqrt2(14))
print(sqrt2(89))

#ex7.3

def tabs(x):   #function tries to format to string and right spacing for table but doesn't really do the spacing part
    return str(x) + 4*' '

def test_square_root(n,m):
    while n <= m:
        a = math.sqrt(n)
        b = sqrt2(n)       
        c = abs(a-b)
        nmbr = tabs(n)
        test1 = tabs(a)
        test2 = tabs(b)
        diff = tabs(c)
        print(nmbr + ' ' + test1 + ' ' + test2 + ' ' + diff)
        n = n + 1
        

test_square_root(1,9)


#ex7.4
def eval_loop ():
    while True:
        x = input('> ')
        if x == 'done':
            break 
        print(eval(x))
        
    print (x)

eval_loop()


#ex7.5
def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
      
def estimate_pi ():
    const = (2*math.sqrt(2))/9801
    k = 1
    sumeval = 1103
    x = sumeval
    while x >= 1e-15:
        x = (factorial(4*k)*(1103+26390*k))/((factorial(k)**4)*(396**(4*k)))
        sumeval += x 
        k = k + 1
    return 1/(const*sumeval)

print(estimate_pi())


