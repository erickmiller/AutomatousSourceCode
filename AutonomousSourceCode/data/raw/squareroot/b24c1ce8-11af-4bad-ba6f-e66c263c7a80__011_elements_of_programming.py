# 1.1 Elements of programming

# 1.1.1 Expressions

# Primitive number expression print(486) 
# Compound expression: numbers combined with primitive procedures
print(12 + 234)
print(1000 - 334)
print(5 * 99)
print(10 / 4.0)
print(2.7 + 10.1)

# Combinations
print((3 + 5) + (10 - 6))
print((3 *
       ((2 * 4) +
        (3 + 5)))
      +
      ((10 - 7) +
       6))
# A name identifies a variable, whose value is the object
pi     = 3.14159
radius = 3.33
print(pi * (radius * radius))

# Name-object associations can be created incrementally
# Here the 'circumference' association uses both 'pi' and 'radius' definitions
circumference = 2 * pi * radius
print(circumference)

# The posibility of associating values with symbols and retrieving them means
# that the interpreter must maintain a memory, that keeps track of
# the name-object pairs. It's called the 'global environment'.

# 1.1.4 Compound procedures

# Procedure definitions - an abstraction technique, by which a compound
# operation can be given a name and then referred to as a unit.
# Example procedure produces the square root of a given value
# The value to be multiplied is given a local name 'x'.
def square(x):
    return x*x
def cube(x):
    return x*x*x

# Square root aproximation

# Calculate average value of two
def average(x, y):
    return (x + y) / 2

# Is current square root aproximation 'good enough' ?
# e.g. differs from expected value with a tolerance level of 0.0001
def is_sqrt_good_enough(x, guess, tolerance=0.0001):
    return abs(square(guess) - x) < tolerance

# Improve current guess value of square root by taking the average of
# the guess and it's quotient with the squared number
def sqrt_improve(x, guess):
    return average(guess, (x / guess))

# Formalize the process of guessing a square root for given value
# Assume that a root guess for any value is 1.0
def sqrt_iter(x, guess = 1.0):
    return guess if is_sqrt_good_enough(x, guess) else sqrt_iter(x, sqrt_improve(x, guess))

print(sqrt_iter(9))

# 1.1.8 Procedures as black box abstractions

# A procedure can have internal definitions, that are local only to
# the procedure. This helps to break up large programs into tractable
# pieces. The 'sqrt' procedure can be rewritten as following
def sqrt_local(x, g=1.0):
    def local_average(x, y): return (x + y) / 2

    def local_good_enough(x, g, t=0.0001): return abs(square(g) - x) < t

    def local_improve(x, g): return local_average(g, (x / g))

    return g if local_good_enough(x, g) else sqrt_local(x, local_improve(x, g))

print(sqrt_local(27))
