import time

start_time = time.time()

txt = open('98.txt').read().split(',')


def is_anagram(a, b):
    """
    Check if a is an anagram of b
    """
    return set(str(a)) == set(str(b))


def is_palindrom(n):
    return str(n)[::-1] == str(n)


#def get_squares(a, b):
#    """
#    Gets the squares between a and b
#    """
#    start, end = a ** 0.5, b ** 0.5
#    for root in xrange(start, end):



def get_square_anagram(a):
    """
    Ex.: 36 ** 2 = 1296 anagram of 9216 = 96 ** 2
    """


lim = int((10 ** 11) ** 0.5)

squares = [i ** 2 for i in range(lim)]
print len(squares)

print time.time() - start_time, 'seconds'
