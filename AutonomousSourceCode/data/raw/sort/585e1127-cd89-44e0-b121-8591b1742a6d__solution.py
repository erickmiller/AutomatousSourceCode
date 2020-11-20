from functools import cmp_to_key
def sort_fractions(fractions):
    return sorted(fractions, key=cmp_to_key(\
        lambda x, y: x[0] * y[1] - x[1] * y[0]))