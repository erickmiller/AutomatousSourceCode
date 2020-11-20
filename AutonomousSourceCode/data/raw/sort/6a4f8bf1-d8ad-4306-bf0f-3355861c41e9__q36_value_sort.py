"""	sort values of a dictionary based on the key	"""


def value_sort(d):
    return [d[x] for x in sorted(d.keys())]

print value_sort({'x': 1, 'y': 2, 'a': 3})

