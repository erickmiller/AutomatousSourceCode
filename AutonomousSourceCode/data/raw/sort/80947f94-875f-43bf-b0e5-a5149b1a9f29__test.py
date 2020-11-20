import random
import copy


def inorder(x):
    i = 0
    j = len(x)
    while i + 1 < j:
        if x[i] > x[i + 1]:
            return False
        i += 1
    return True


def sort(x):
    # BEGIN
    random.shuffle(x)
    return x
    # END


# Generate random sequence
sorted_seq = [x for x in range(10) if random.choice([True, False])]

unsorted_seq = copy.copy(sorted_seq)
random.shuffle(unsorted_seq)

assert sorted_seq == sort(unsorted_seq)
