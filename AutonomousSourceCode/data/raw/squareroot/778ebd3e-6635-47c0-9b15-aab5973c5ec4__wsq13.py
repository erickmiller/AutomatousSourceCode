def RootBab(num):
    n = num
    r = 1
    acc = 0.0000001
    while (n - r) > acc:
        n = (n + r)/2
        r = num/n
    return n
 
x = float(input("Of which number should I calculate the square root? "))
print("The square root of",x,"is",RootBab(x))
