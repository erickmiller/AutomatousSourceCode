#function that evaluates the following equation given A, C, and n
"""
(1 + sqrt(1 + C * n)) / A
"""
#returns True if result would be an integer
def has_int_root(n, V):
    A, C = V
    square = 1 + C * n
    sq_root = int(square ** 0.5 + 0.5)
    #in order for expression to be an integer, sq_root must be integer
    if sq_root ** 2 != square:
        return False
    num = 1 + sq_root
    #test if integer
    if int(num / A + 0.5) * A == num:
        return True
    return False

