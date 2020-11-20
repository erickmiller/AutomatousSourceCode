#7.1
def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print("Blastoff!")


#7.2
def square_root(a):
    if(a == 0 or a == 1):
        return a
    elif(a > 1):
        x = a/2
        epsilon = 0.0000001
        while True:
            y = (x + a/x)/2
            if abs(y-x) < epsilon:
                return y
                break
            x = y
    else:
        return "Invalid Input"
        

#7.3
import math
def square_root(a):
    x = a/2
    epsilon = 0.0000000001
    while True:
        y = (x + a/x) / 2
        if abs(x - y) < epsilon:
            return y
            break
        x = y

def test_square_root(a):
        print(a, square_root(a), math.sqrt(a), abs(square_root(a) - math.sqrt(a)))


#7.4
def eval_loop():
    x = ""
    result = 0
    while True:
        x = input("Give me math > ")
        if x == 'done':
            break
        result = eval(x)
        print(result)
    return result

#7.5
import math

def factorial(n):
    if n == 0:
        return 1
    else:
        value = factorial(n-1)
        return n*value

def estimate_pi():
    total = 0
    k = 0
    left_side = 2*math.sqrt(2)/9801
    while True:
        num = factorial(4*k) * (1103+26390*k)
        den = factorial(k)**4 * 396**(4*k)
        term = left_side * num / den
        total += term                
        if abs(term) < 1e-16:
            break
        k += 1
    return 1 / total
    
print(estimate_pi(), math.pi)



    





    


        
        


        
