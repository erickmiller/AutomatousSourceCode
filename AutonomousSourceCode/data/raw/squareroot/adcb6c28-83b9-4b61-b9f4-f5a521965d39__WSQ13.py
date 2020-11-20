def babylon(num):
    n = num
    r = 1
    accuracy = 0.000001
    while (n - r) > accuracy:
        n = (n + r)/2
        r = num/n
    return n
a = float(input("Write the number you want the squareroot of: "))
print(("The square root of ")+str(a)+(" is: ")+str(babylon(a)))
