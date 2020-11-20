def newtonSqrt(n):
    '''Calculates the square root of n'''
    
    i = 0
    approx = n / 2
    better_approx = 0.5 * (approx + (n / approx))

    while better_approx != approx:
        
        approx = better_approx
        better_approx = 0.5 * (approx + (n / approx))
        i = i + 1
        print(better_approx, "number of iterations: ", i)

    return approx

number = float(input("Enter the number: "))

print("Square root of the number is: ", newtonSqrt(number))
