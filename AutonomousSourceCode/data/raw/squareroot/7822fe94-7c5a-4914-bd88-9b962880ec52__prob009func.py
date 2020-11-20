def is_square(test):
    from math import sqrt
    root = sqrt(test)

    if int(root) == root: return True
    else: return False
