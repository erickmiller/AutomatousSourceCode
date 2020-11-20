#   Conor T. Ryan
#   Week 5 Homework
#   UW PCE Programming in Python
#   Fall 2011 (Jacky)

from copy import copy

def sorted_list(listToSort):

    sortedList = []

    # 1st method: build new list from passed list
    #
    # for listItem in listToSort:
    #     sortedList.append(listItem)

    # copy the list and prove it's a copy
    sortedList = copy(listToSort)
    assert sortedList is not listToSort

    # sort the thing
    sortedList.sort()

    return sortedList

if __name__ == '__main__':

    list1 = ['z', 'x', 'y']
    list2 = ['banana', 'pear', 'apple']

    newList1 = sorted_list(list1)
    newList2 = sorted_list(list2)

    assert list1 == ['z', 'x', 'y']
    assert list2 == ['banana', 'pear', 'apple']

    print newList1
    print newList2
    print list1
    print list2
