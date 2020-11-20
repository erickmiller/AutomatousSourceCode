"""
:Author: fcp
:Date: 3/24/2011
"""

from pychm.tools import Property


class Bond(object):
    """
    DOCME
    """
    def __init__(self, atom1, atom2):
        """
        DOCME
        """
        super(Bond, self).__init__()
        self._data = sorted([atom1, atom2])

    @Property
    def i():
        doc =\
        """
        DOCME
        """
        def fget(self):
            return self._data[0]
        return locals()

    @Property
    def j():
        doc =\
        """
        DOCME
        """
        def fget(self):
            return self._data[1]
        return locals()

    @Property
    def key():
        doc =\
        """
        DOCME
        """
        def fget(self):
            return (self.i.addr, self.j.addr)
        return locals()

    @Property
    def length():
        doc =\
        """
        DOCME
        """
        def fget(self):
            i, j = self._data
            return i.calc_length(j)
        return locals()

    def _sort(self):
        return 1e12 * self.i._sort() + self.j._sort()

    def __repr__(self):
        return '%s%r' % (self.__class__.__name__, self.key)

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self._data == other._data

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self._sort() < other._sort()

    def __le__(self, other):
        return self._sort() <= other._sort()

    def __gt__(self, other):
        return self._sort() > other._sort()

    def __ge__(self, other):
        return self._sort() >= other._sort()

