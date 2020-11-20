###Lambda is used when we need to return a function from within a function. 
# That means that Python has two tools for building functions: def and lambda.
#It is an expression that is simply a function without a name - its an anonymous function
#lambda arg1, arg2, ...argN : expression using arguments
def square_root(x): return math.sqrt(x)
#or
square_root = lambda x: math.sqrt(x)

def p(t):
    return t*2

print p(2)
print p(3)

#Equivalent Lambda function
#lambda x:x**2 is the actual function
#y only contains the function and itself is NOT a function
y=lambda x:x**2

print y(2)


###Ex3:
f = lambda x, y : x + y
f(1,1)

###Ex4:
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)


###Ex5:
mz = (lambda a = 'Wolfgangus', b = ' Theophilus', c = ' Mozart': a + b + c)
mz('Wolfgang', ' Amadeus')
