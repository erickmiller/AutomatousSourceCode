def square_root(a):
    epsilon = 0.0000001
    x = a / 2
    while True:
        print(x)
        y = (x + a/x) / 2
        print(y)
        if abs(y-x) < epsilon:
            #break
            return y
        else:
            x = y
    #return x

print(square_root(25))
