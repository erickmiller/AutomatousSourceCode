EPSILON = 0.000001

def square_root(num):
    low = 0.0
    high = 1.0 + (num / 2.0)

    while low < high:
        mid = (low + high) / 2
        sqr = mid ** 2
        diff = abs(num - sqr)

        if diff <= EPSILON:
            return mid

        if sqr < num:
            low = mid
        else:
            high = mid

    return -1

print square_root(256)
