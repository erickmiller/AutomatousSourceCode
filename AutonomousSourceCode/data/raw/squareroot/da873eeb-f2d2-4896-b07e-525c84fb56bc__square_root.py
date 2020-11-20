import pandas as pd
from bokeh.charts import Line, output_file, show


iterations = 0
difference = []
output_file("lines.html")


def square(x):
    return x * x


def average(x, y):
    return (x + y) / 2


def improve(guess, x):
    return average(guess, (x / guess))


def good_enough(guess, x):
    global difference
    difference.append(abs(square(guess) - x))
    return abs(square(guess) - x) < 0.001


def square_root_iter(guess, x):
    global iterations
    iterations += 1
    if good_enough(guess, x):
        return guess
    else:
        return square_root_iter(improve(guess, x), x)


def square_root(x):
    return square_root_iter(1.0, x)


square_root(100)
data = {"y": difference}
p = Line(data, title="Newton Square Root", xlabel="iterations", ylabel="difference", width=400, height=400)
