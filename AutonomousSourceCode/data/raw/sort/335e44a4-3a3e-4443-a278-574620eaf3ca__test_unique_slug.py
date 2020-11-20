import random
import copy

def sort(seq):
# BEGIN
    return sorted(seq)
# END

# Generate random sequence
sorted_seq = [x for x in range(10) if random.choice([True, False])]

unsorted_seq = copy.copy(sorted_seq)
random.shuffle(unsorted_seq)

assert sorted_seq == sort(unsorted_seq)
