def square_root(x):
    def square(y):
        return y * y


    def average(x, y):
        return (x + y) / 2


    def improve(guess):
        return average(guess, (x / guess))


    def good_enough(guess):
        return abs(square(guess) - x) < 0.00001


    def square_root_iter(guess):
        if good_enough(guess):
            return guess
        else:
            return square_root_iter(improve(guess))


    return square_root_iter(1.0)

print(square_root(2))
