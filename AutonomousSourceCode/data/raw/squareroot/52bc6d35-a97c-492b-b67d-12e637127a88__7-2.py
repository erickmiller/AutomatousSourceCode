def square_root(a):
    x = a / 2
    epsilon = .000000001
    while True:
        y = (x + a/x) / 2
        print "x:" + str(x) + " y:" + str(y)
        if abs(y-x) < epsilon:
            return y
        x = y


print square_root(125.0)