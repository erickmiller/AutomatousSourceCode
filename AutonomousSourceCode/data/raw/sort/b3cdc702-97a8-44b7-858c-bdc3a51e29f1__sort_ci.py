
from operator import attrgetter

class CI_name(object):
    def __init__(self, name):
        self.name = name
        self.ci_name = name.lower()

def sorted_ci(iterable):
    ls = map(CI_name, iterable)
    ls.sort(key=attrgetter("ci_name"))
    return [el.name for el in ls]

## second implementation:

def sorted_ci(iterable):
    ls = [(name.lower(), name) for name in iterable]
    ls.sort()
    return [el[1] for el in ls]

if __name__ == "__main__": # test
    ls = "ciao Nina come Va?".split()
    print sorted(ls)
    print sorted_ci(ls)

