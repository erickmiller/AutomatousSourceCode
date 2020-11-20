def square_root(s):
    i = 1
    j = s
    while (abs(j - i) > 0.001):
        print i, j
        j = (i + j) / 2.0
        i = s * 1.0/j
    return i

print square_root(100)
