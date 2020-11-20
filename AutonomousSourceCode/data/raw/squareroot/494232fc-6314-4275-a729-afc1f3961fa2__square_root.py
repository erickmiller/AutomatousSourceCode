def newton_sq_rt(root_of):
    '''Finds square root to minimum precision of 0.01 using Newton's method
        of successive approximations'''

    # Start with initial guess of half the input value
    apxroot = root_of/2
    n = 0
    while abs(root_of - apxroot**2) > 0.01:
        if n == 0: # I like to be grammatically correct :smiley:
            print("{} iteration,  guess is {}".format(n+1, round(apxroot,2)))
        else:
            print("{} iterations, guess is {}".format(n+1, round(apxroot,2)))
        apxroot  = (apxroot + root_of/apxroot)/2
        n += 1
    return apxroot

def get_input():
    root_of = input("Enter a number: ")
    try:
        float(root_of)
    except:
        print("Non-numeric input.".format(end=''))
        return get_input()
    if float(root_of) < 0:
        print("Negative number; result is type 'complex'.")
        return abs(float(root_of)), True
    return float(root_of), False

root_of, complex_bool = get_input()
if complex_bool:
    print("The square root of -{} is {}j".format(root_of, round(newton_sq_rt(root_of),2)))
else:
    print("The square root of {} is {}".format(root_of, round(newton_sq_rt(root_of),2)))
