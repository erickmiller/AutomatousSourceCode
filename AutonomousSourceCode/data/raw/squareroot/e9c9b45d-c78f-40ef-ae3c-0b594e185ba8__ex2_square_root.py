def square_root(a):
    
    x = 3
    epsilon = 0.000000000001
    while True:
        y = (x + a/x) /2
        if abs(y-x) < epsilon:
            break
        x = y
    return x


if __name__ == '__main__':
    print(square_root(49))
