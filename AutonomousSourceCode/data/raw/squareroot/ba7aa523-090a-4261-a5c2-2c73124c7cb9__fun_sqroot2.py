#square root function with check condition

#function definition
def sqroot(x):
    if x <= 0:
        print "Positive number only."
        return

    sqrt = x**0.5     #square root
    print "Square root of ", x, " is ", sqrt

#input
x = input("Enter x: ")

#function call
sqroot(x)
