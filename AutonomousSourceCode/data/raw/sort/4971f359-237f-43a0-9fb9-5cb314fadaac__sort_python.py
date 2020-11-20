import fileinput
from random import shuffle
from timer import Timer

l = []
for i in fileinput.input():
    l.append(int(i))

def sort_python(l):
    return sorted(l)

with Timer() as t:
    l = sort_python(l)

print l
print('List length: %i' % len(l))
print('Sort time: %.05fs' % t.interval)