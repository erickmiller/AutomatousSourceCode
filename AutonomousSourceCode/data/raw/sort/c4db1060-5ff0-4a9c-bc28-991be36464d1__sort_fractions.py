#!/usr/bin/env python3


def tuples_divisions(fractions):
    divisions = []
    for fraction in fractions:
        x, y = fraction
        divisions.append(x / y)
    return divisions


def combine_tuples_and_divisions(fractions):
    fractions_dict = {}
    for index, pair in enumerate(fractions):
        fractions_dict[tuples_divisions(fractions)[index]] = fractions[index]
    return fractions_dict


def sort_fractions(fractions):
    sorted_fractions = []
    sorted_by_key = sorted(combine_tuples_and_divisions(fractions).items(),
                           key=lambda t: t[0])
    for index, result in enumerate(sorted_by_key):
        sorted_fractions.append(result[1])
    return sorted_fractions


def main():
    print(sort_fractions([(5, 6), (22, 78), (22, 7),
                          (7, 8), (9, 6), (15, 32)]))

if __name__ == '__main__':
    main()
