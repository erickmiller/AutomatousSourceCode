def sort_fractions(fractions):
    s = sorted(fractions, key = lambda x: x[0]/x[1])
    return s


def main():
    print (sort_fractions([(2, 3), (1, 2)]))
    print (sort_fractions([(2, 3), (1, 2), (1, 3)]))
    print (sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))


if __name__ == '__main__':
    main()
