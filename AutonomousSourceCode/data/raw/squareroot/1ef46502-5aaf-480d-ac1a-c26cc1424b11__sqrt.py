"""Exercise 7.2. Encapsulate this loop in a function called square_root that takes a as a parameter,
chooses a reasonable value of x, and returns an estimate of the square root of a."""

def my_square_root(a,x) :
    e = 0.0001
    while True :
        y=(x+a/x)/2
        if abs(y-x) < e :
            return y
            break
        x = y

a = input("Find square root of which number? ",)
x = input("What is your first guess?")    
result = round(my_square_root(float(a),float(x)),3)
print("The square root of ",a,"is ",result)
