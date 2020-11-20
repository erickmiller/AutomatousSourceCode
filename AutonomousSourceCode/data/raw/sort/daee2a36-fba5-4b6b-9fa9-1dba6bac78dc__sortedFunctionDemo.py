__author__ = 'luowen'

# sorted function return a new sorted list from the items in iterable.
# sorted(iterable, key, reverse)
# key is a function for customer compare
# reverse is Boolean type True is reverse iterable False is common sort
# see the example


list1 = [1, 3, 4, 55, 2, 233, 21, 22]

def key(x):
    if x < 20:
        return True
    else:
        return False
resultSet = sorted(list1, key=key)
print(resultSet)  # [55, 233, 21, 22, 1, 3, 4, 2]

resultSet = sorted(list1)
print(resultSet)  # [1, 2, 3, 4, 21, 22, 55, 233]

resultSet = sorted(list1, reverse=True)
print(resultSet)  # [233, 55, 22, 21, 4, 3, 2, 1]

set1 = {"a", "x", "c", "d"}

resultSet = sorted(set1)
print(resultSet)





# sortedList1 = sorted(list1, reverse=True)
# print(sortedList1)
