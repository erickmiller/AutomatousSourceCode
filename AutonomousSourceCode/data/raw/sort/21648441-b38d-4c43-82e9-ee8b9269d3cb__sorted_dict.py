from nocassa.cassandra.genbisect import insort


class SortedDict(dict):
    def __init__(self, *args, **kwargs):
        sup = super(SortedDict, self)
        sup.__init__(*args, **kwargs)
        self.sorted_keys = sup.keys()
        self.sort_keys()

    def sort_keys(self):
        self.sorted_keys.sort(cmp=self.compare)

    def insort(self, key):
        insort(self.sorted_keys, key, compare=self.compare)

    def remove_key(self, key):
        self.sorted_keys.remove(key)

    compare = staticmethod(cmp)

    def __delitem__(self, key):
        super(SortedDict, self).__delitem__(key)
        self.remove_key(key)

    def __eq__(self, other):
        if not super(SortedDict, self).__eq__(other):
            return False
        if isinstance(other, SortedDict):
            return other.sorted_keys == self.sorted_keys
        return True

    def __iter__(self):
        for k in self.sorted_keys:
            yield k

    def __ne__(self, other):
        return not self.__eq__(other)

    def __setitem__(self, key, value):
        if key not in self:
            self.insort(key)
        super(SortedDict, self).__setitem__(key, value)

    def __repr__(self):
        r = ', '.join(': '.join(map(repr, item)) for item in self.iteritems())
        r = '%s({%s})' % (self.__class__.__name__, r)
        return r

    def clear(self):
        self.sorted_keys[:] = []
        super(SortedDict, self).clear()

    def copy(self):
        return self.__class__(self)

    @classmethod
    def fromkeys(cls, S, v=None):
        return cls(super(SortedDict, cls).fromkeys(S, v))

    def iteritems(self):
        for k in self:
            yield (k, self[k])

    iterkeys = __iter__

    def itervalues(self):
        for k in self:
            yield self[k]

    def keys(self):
        return list(self.sorted_keys)

    def items(self):
        return list(self.iteritems())

    def pop(self, *args):
        pop = super(SortedDict, self).pop
        if len(args) not in [1, 2]:
            pop(*args)

        if len(args) == 1:
            k, = args
            value = pop(k)
            self.remove_key(k)
            return value

        k, d = args
        if k in self:
            self.remove_key(k)

        return pop(k, d)

    def values(self):
        return list(self.itervalues())
