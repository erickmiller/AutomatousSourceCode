from __future__ import division
import sys
import os
import matplotlib.pyplot as plt

mydir = os.path.expanduser("~/")


def closest_perfect_square(n):
    """ http://stackoverflow.com/questions/15390807/integer-square-root-in-python """
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def WebsterLocey(x):
    y1 = closest_perfect_square(x)

    y2 = y1 + 1
    z1 = x - y1**2
    z2 = y1 + y2
    a = y + z1/z2

    return float(a)


fig = plt.figure()
ax = fig.add_subplot(2,2,1)

x = 1
xs = []
sqrts = []
WLs = []

for i in range(100):

    xs.append(x)
    y = x**0.5
    sqrts.append(y)
    a = WebsterLocey(x)
    WLs.append(a)
    x += 1
	
sqrts - WLs

plt.scatter(xs, sqrts, s=50, color='m', facecolors='none', label='square root')
plt.scatter(xs, WLs, color='c', alpha=0.9, label='W&L rule')
#plt.yscale('log')
#plt.xscale('log')
plt.xlabel('x', fontsize=8)
plt.ylabel('y', fontsize=8)
leg = plt.legend(loc=2,prop={'size':12})
leg.draw_frame(False)
plt.text(-50, 14, "How well does the Webster-Locey Rule approximate square roots?", fontsize=16)




