import collections

def key_sort_dictionary(d):
    """

    Python's `dict` type doesn't support ordering.

    :param d: A dictionary.

    :returns: OrderedDictionary.
    """

    return collections.OrderedDict(sorted(d.items(), key=lambda t: t[0]))
