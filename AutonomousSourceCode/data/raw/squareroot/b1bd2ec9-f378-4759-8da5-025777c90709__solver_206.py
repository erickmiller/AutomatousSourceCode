def solver():
    """ Find the unique positive integer whose square has the form
    1_2_3_4_5_6_7_8_9_0 where _ is a single digit

    We can find the maximum and minimum boundary of square roots
    that satisfy 1020304050607080900 < n ** 2 < 1929394959697989990

    Note that a square ending in "0" has to end in at least "00",
    therefore we can simplify the problem to fnding the bounds of
    10203040506070809 < n ** 2 < 19293949596979899 and then multiplying
    the square root by 10
    
    (solved 2014-11-29)
    """
    min_bound = int(10203040506070809 ** 0.5)
    max_bound = int(19293949596979899 ** 0.5) + 1

    for number in xrange(min_bound, max_bound):
        if str(number ** 2)[::2] == "123456789":
            return number * 10  # multiply back by 10

solver()