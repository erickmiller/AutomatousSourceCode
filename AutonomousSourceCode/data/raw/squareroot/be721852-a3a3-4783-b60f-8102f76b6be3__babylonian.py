def babylonian(a):
    r = a
    while (p > q):
        p = (p + q)/2.0
        q = r/p
    return p

a = float(input("Introduce a number: "))
b = babylonian(a)

print ("The babylonian square root of ", a, " is ", b)
