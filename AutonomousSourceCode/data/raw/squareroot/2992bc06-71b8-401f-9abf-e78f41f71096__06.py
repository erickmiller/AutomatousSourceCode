# General iterative solving, recursive version I
# ----------------------------------------------
def iter_solve(guess, done, update):
    """Return the result of repeatedly applying UPDATE, 
    starting at GUESS, until DONE yields a true value 
    when applied to the result.  UPDATE takes a guees
    and returns an updated guess."""
    if done(guess):
        return guess
    else:
        return iter_solve(update(guess), done, update)

# General iterative solving, recursive version II
# -----------------------------------------------
def iter_solve(guess, done, update):
    """Return the result of repeatedly applying UPDATE, 
    starting at GUESS, until DONE yields a true value 
    when applied to the result.  UPDATE takes a guees
    and returns an updated guess."""
    def solution(guess):
        if done(guess):
            return guess
        else:
            return solution(update(guess))
    return solution(guess)

# General iterative solving, iterative version
# --------------------------------------------
def iter_solve(guess, done, update):
    """Return the result of repeatedly applying UPDATE, 
    starting at GUESS, until DONE yields a true value 
    when applied to the result.  UPDATE takes a guees
    and returns an updated guess."""
    while not done(guess):
        guess = update(guess)
    return guess

# General iterative solving with iteration limit, recursive
# ---------------------------------------------------------
def iter_solve(guess, done, update, iteration_limit=32):
    """Return the result of repeatedly applying UPDATE, 
    starting at GUESS, until DONE yields a true value 
    when applied to the result.  Causes error if more than
    ITERATION_LIMIT applications of UPDATE are necessary."""

    def solution(guess, iteration_limit):
        if done(guess):
            return guess
        elif iteration_limit <= 0:
            raise ValueError("failed to converge")
        else:
            return solution(update(guess), iteration_limit-1)
    return solution(guess, iteration_limit)

# General iterative solving with iteration limit, iterative
# ---------------------------------------------------------
def iter_solve(guess, done, update, iteration_limit=32):
    """Return the result of repeatedly applying UPDATE, 
    starting at GUESS, until DONE yields a true value 
    when applied to the result.  Causes error if more than
    ITERATION_LIMIT applications of UPDATE are necessary."""

    while not done(guess):
        if iteration_limit <= 0:
            raise ValueError("failed to converge")
        guess, iteration_limit = update(guess), iteration_limit-1
    return guess

# Direct implementation of square root using Newton's method
# ----------------------------------------------------------
def square_root(x):
    """Compute an approximation to the square root of X.
    >>> round(square_root(9), 10)   # round to 10 decimal places
    3.0
    """
    if x < 0:
        raise ValueError("square root of negative value")
    tol = abs(x) * 1.0e-10
    y = x * 0.5
    while abs(y*y - x) > tol:
        y -= (y * y - x) / (2.0 * y)    # y = y - (y*y - x)/ (2.0 * y)
    return y

# General Newton's method
# -----------------------
def newton_solve(func, deriv, start, tolerance):
    """Return x such that |FUNC(x)| < TOLERANCE, given initial
    estimate START and assuming DERIV is the derivatative of FUNC."""
    def close_enough(x):
        return abs(func(x)) < tolerance
    def newton_update(x):
        return x - func(x) / deriv(x) 

    return iter_solve(start, close_enough, newton_update, 1000000000)

def square_root(a):
    """Compute an approximation to the square root of A.
    >>> round(square_root(9), 10)   # round to 10 decimal places
    3.0
    """
    if a < 0:
        raise ValueError("square root of negative value")
    return newton_solve(lambda x: x*x - a, lambda x: 2 * x, 
                        a/2, a * 1e-10)

def cube_root(a):
    """Compute an approximation to the cube root of X.
    >>> round(cube_root(8), 10)   # round to 10 decimal places
    2.0
    """
    return newton_solve(lambda x: x**3 - a, lambda x: 3 * x ** 2,
                        a/3, a * 1e-10)

# Secant method
# -------------
def iter_solve2(guess, done, update, state=None):
    """Return the result of repeatedly applying UPDATE to GUESS
    and STATE, until DONE yields a true value when applied to
    GUESS and STATE.  UPDATE returns an updated guess and state."""
    while not done(guess, state):
        guess, state = update(guess, state)
    return guess

def secant_solve(func, start0, start1, tolerance):
    """An approximate solution to FUNC(x) == 0 for which
    |FUNC(x)|<TOLERANCE, as computed by the secant method
    beginning at points START0 and START1."""
    
    def close_enough(x, state):
        return abs(func(x)) < tolerance
    def secant_update(xk, xk1):
        return (xk - func(xk) * (xk - xk1) 
                                / (func(xk) - func(xk1)), 
                xk)
    return iter_solve2(start1, close_enough, secant_update, start0)

def square_root2(x):
    """An approximation to the square root of X, using the secant method.
    >>> round(square_root2(9), 10)
    3.0
    """
    if x < 0:
        raise ValueError("square root of negative value")
    return secant_solve(lambda y: y*y - x, 1, 0.5 * (x + 1), x * 1.0e-10)

