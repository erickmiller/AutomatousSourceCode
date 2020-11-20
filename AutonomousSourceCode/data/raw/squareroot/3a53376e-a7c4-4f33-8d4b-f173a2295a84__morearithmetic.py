def add(token):
    tot = 0
    for i in range(1,len(token)):
        tot = tot + float(token[i]) 
    return tot

def subtract(token):
    tot = float(token[1])
    for i in range(2,len(token)):
        tot = tot - float(token[i]) 
    return tot

def multiply(token):
    product = 1
    for i in range(1, len(token)):
        product = product * float(token[i])
    return product

def divide(token):
    quo = float(token[1])
    for i in range(2, len(token)):
        quo = quo / float(token[i])
    return quo

def square(token):
    return float(token[1])*float(token[1])

def cube(token):
    return float(token[1]) ** 3

def power(token):
    base = float(token[1])
    for i in range(2,len(token)):
        base = base ** float(token[i])
    return base

def mod(token):
    return float(token[1]) % float(token[2])

def root(token):
    return float(token[1])**(1/float(token[2]))
