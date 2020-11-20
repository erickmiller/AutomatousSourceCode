#!/usr/bin/python
def fact(n):
    if n >= 0:
        return fact2(n, 1)
    else:
        raise ValueError("Input must be more than or equal to 0")
def fact2(a, b):
    if a != 1:
        return fact2(a - 1, b * a)
    else:
        return b
    
def fib(n):
    if n >= 0:
        return fib2(n, 0, 1)
    else:
        raise ValueError("Input must be more than or equal to 0")
def fib2(a, b, c):
    if a != 1:
        return fib2(a - 1, c, b + c)
    else:
        return b

def sqrt(n):
    if n > 0:
        return sqrt2(n, 1)
    elif n == 0:
        return 0
    else:
        raise ValueError("Input must be more than or equal to 0")

def sqrt2(a, b):
    if abs(a - b * b) > .000000000000001:
        return sqrt2(a, (a/b + b)/2)
    else:
        return b

print("Factorial of 10")    
print(fact(10))
print("Fib of 20")
print(fib(20))
print("Square root of 625")
print(sqrt(625))
