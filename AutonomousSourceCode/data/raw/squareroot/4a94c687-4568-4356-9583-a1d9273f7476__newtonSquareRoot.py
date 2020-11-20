#newton square root

#function definition
def sqrt(n):
    approx = n/2.0
    better = (approx + n/approx)/2.0
    while better != approx:
        approx = better
        better = (approx + n/approx)/2.0
    return approx

x = input("Enter x: ")
print "Square Root: ", sqrt(x)
