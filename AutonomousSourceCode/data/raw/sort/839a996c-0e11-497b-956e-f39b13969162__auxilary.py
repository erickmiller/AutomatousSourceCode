import random

def sorted_(list_):
    return all(list_[i] <= list_[i+1] for i in xrange(len(list_) - 1))
def generate_(n = 10, k = 10):
    return [random.randrange(0, k) for _ in range(0, n)]
def swap(list_, left, right):
    temp = list_[left]
    list_[left] = list_[right]
    list_[right] = temp
def run_algorithm(list_, sort_function):
    for i in list_:
        sort_function(list_)
        if not sorted_(list_): return False
    return True
