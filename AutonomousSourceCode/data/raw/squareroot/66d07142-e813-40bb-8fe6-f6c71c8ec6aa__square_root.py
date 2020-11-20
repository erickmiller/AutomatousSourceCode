def square_root(x, eps):
    ''' (float, float) -> float
    Return the square root of x to within "the accuracy" of eps.
    '''
    counter = 0
    this_guess = 1.0
    next_guess = 0.5 * (this_guess + (x / this_guess))
    error = next_guess - this_guess
    while abs(error) > eps and counter <= 10:
        this_guess = next_guess
        next_guess = 0.5 * (this_guess + (x / this_guess))
        error = next_guess - this_guess
        counter += 1
    if counter <= 10:
        return next_guess
    else:
        return -1
