__author__ = 'Shane'
# calculates the median of a list of numbers


def mymedian(l):
    sorted_list = l
    sorted_list.sort()

    if len(l) % 2 == 1:
        return sorted_list[int((len(l) - 1) / 2)]
    else:
        m = int(len(l) / 2)
        return (sorted_list[m] + sorted_list[m - 1]) / 2

print(mymedian([4, 6, 6, 6, 0, 111, 111, 222, 333, 444]))
