def squareRoot(num, epsilon):
    iteration = 0
    result = 0.0
    while abs(result ** 2 - num) > epsilon and result < num:
        result += epsilon ** 2
        iteration += 1
    print iteration
    return result

print squareRoot(25, 0.1)