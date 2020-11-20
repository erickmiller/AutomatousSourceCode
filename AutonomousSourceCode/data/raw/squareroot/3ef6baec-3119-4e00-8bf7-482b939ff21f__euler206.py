__author__ = 'jianxinsun'

import math


def check(n):
    square = str(n * n)
    return all(int(square[x * 2]) == x + 1 for x in range(9))


root_max = int(19293949596979899 ** 0.5 / 10)
root_min = int(10203040506070809 ** 0.5 / 10)

print root_max
print root_min

for i in range(root_min, root_max + 1):
    if check(i * 10 + 3):
        print i * 100 + 30
        break
    else:
        if check(i * 10 + 7):
            print i * 100 + 70
            break


# def match(n):
#     s = str(n)
#     return not all(int(s[x*2]) == x+1 for x in range(9))
#
#
# n = int(10203040506070809**0.5)    # sqrt(19293949596979899)
# while match(n*n): n += 2
#
# print "Project Euler 206 Solution =", n*10    #add the trailing zero