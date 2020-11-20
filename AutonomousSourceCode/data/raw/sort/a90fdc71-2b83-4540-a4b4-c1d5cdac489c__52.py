def SortedList(input):
    temp = list(str(input))
    temp.sort()
    return temp


i = 1
while True:
    if SortedList(i) == SortedList(2 * i) == SortedList(3 * i) == SortedList(4 * i) == SortedList(5 * i) == SortedList(
                    6 * i):
        print(i)
        break
    i += 1