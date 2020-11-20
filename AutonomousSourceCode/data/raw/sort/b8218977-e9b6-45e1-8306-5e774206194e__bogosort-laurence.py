import random, itertools

def bogosort(l):
    '''
    Randomly shuffles a list, in-place, repeatedly until it's sorted.
    '''
    while not is_sorted(l):
        random.shuffle(l)

def is_sorted(l):
    '''
    Checks if a list is sorted.
    '''
    for i, j in itertools.izip(l, l[1:]):
        if i > j:
            return False
    return True

def test():
    sort_these = [1, 3, 2, 4]

    print sort_these
    bogosort(sort_these)
    print sort_these

if __name__ == '__main__':
    test()
