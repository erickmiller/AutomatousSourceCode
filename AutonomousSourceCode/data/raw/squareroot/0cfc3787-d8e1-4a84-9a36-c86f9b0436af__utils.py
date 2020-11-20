import math

#######################
# Statistical helpers #
#######################

def avg(vals):
    """Calculate average of values in list."""
    return sum(vals) / float(len(vals))


def disp(y_1, y_2):
    """Calculate sum of differences between f[] and y[] values."""
    total = 0
    for i in range(min(len(y_1),
                       len(y_2))):
        total += (y_1[i] - y_2[i]) ** 2

    return total

def std(y_1, y_2):
    """Calculate square root of dispersion."""
    return math.sqrt(disp(y_1, y_2))
