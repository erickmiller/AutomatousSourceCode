__author__ = 'D'
'''
Intent: Define a family of algorithms, encapsulate each one, and make them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.
[Copied from GOF Site]

For this implementation I will create two sorting algorithms for different value types: least first and greatest first
I will then hand one of these to a SorterClass, whose data will be in string form and the sorting Algortihms
will be called uniformly.
'''

class SortingStrategy():
    def sort(self,listToSort):
        pass

class LeastFirstStrategy(SortingStrategy):
    def sort(self,listToSort):
        return sorted(listToSort)

class GreatestFirstStrategy(SortingStrategy):
    def sort(self,listToSort):
        return sorted(listToSort,reverse=True)


class SortUser():
    _itemsToSort = 1,3,2,5,0,4

    def __init__(self,sortingMethod):
        self.sortMethod = sortingMethod

    def returnSortedItems(self):
        return self.sortMethod.sort(self._itemsToSort)


def demonstrate():
    leastSort = SortUser(LeastFirstStrategy())
    greatSort = SortUser(GreatestFirstStrategy())

    print("Least Sort: ")
    print(leastSort.returnSortedItems())
    print("Great Sort: ")
    print(greatSort.returnSortedItems())

if __name__ == '__main__':
    demonstrate()