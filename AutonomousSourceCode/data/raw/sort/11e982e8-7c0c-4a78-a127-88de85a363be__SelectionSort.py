#!/usr/env python
#
# Implementation of the Selection-Sort algorithm

class SelectionSort:
    """Implementation class for Selection sort."""

    @staticmethod
    def selectionSort( listToSort ):
        """Implementation of the algorithm.
        
        @param  listToSort  The list to sort.
        @return The sorted list
        """
        res = []
        ok = True
        while ok:
            if listToSort:
                minimum = min(listToSort)
                res.append( minimum )
                listToSort.remove( minimum )
            else:
                ok = False
        return res


def main():
    """Main-method, does testing."""
    import random
    l = []
    for i in range(20):
        l.append( random.randint( 0, 100))

    print( "List of random values: " + str(l) )
    print( " ### Sorting ... done." )
    res = SelectionSort.selectionSort( l )
    print( "Sorted list: " + str(res) )


if __name__ == "__main__":
    main()
