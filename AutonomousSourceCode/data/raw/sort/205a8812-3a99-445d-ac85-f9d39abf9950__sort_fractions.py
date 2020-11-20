def evaluate_fraction(fraction):
    return fraction[0] / fraction[1]


def sort_fractions(fractions):
    return(sorted(fractions, key=evaluate_fraction))
