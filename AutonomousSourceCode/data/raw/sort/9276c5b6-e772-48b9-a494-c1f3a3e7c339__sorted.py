class MyDict:
    def __init__(self, d = {}):
        self.dict = d

    def keys(self):
        """
        >>> a = MyDict({'a': 1, 'b': 2, 'c': 3})
        >>> a.keys()
        ['a', 'b', 'c']
        """
        sorted_keys = self.dict.keys()
        sorted_keys.sort()
        return sorted_keys

    def values(self):
        """
        >>> a = MyDict({'a': 1, 'b': 2, 'c': 3})
        >>> a.values()
        [1, 2, 3]
        """
        sorted_values = self.dict.values()
        sorted_values.sort()
        return sorted_values



def main():
    d = MyDict({'a' : 1, 'b' : 2, 'c' : 3})
    print( d.keys() )
    print( d.values() )

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
