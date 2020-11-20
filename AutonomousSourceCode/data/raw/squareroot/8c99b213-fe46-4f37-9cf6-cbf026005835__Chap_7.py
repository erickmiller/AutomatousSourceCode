import math

## 7. 1

def print_n(s, n) :
    while n > 0 :
        print s
        n = n -1 
    return None


## 7. 2

def square_root(a, x) :
    """
    a : number to compute square root
    x : approximation guess
    """
    while True :
        #print x
        y = (x + a/x) / 2
        if abs(y - x) < 0.000000001 :
            break
        x = y
    return x

## 7. 3

def test_square_root(a, x) :
    result = square_root(a,x)
    right = math.sqrt(a)
    diff = abs(result - right)
    print a, result, right, diff

## 7.4

def eval_loop() :
    while True :
        a = raw_input('Give me a sting to evaluate : \n')
        if a == 'done' :
            break
        r = eval(a)
        print r
    return r


## 7. 5

def estimate_pi() :
    s = 0
    k = 0
    while True :
        time = 2*math.sqrt(2)/9810
        numer = math.factorial(4*k) * (1103 + 26390*k)
        denom = (math.factorial(k))**4 * 396**(4*k)
        if time * numer / denom < 1e-15 :
            break
        s = s + time * numer / denom
        k = k + 1
    pi = 1/s
    return pi
        
