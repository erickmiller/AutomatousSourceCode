__author__ = 'Lucian'
from const import values


def sort_high_to_low(shuffle_cards):
    sort_cards = []
    for value in values:
        for i, card in enumerate(shuffle_cards):
            if card[0] == value:
                sort_cards.append(shuffle_cards[i])
    return sort_cards


def type_color(card):
        return card[1]


def sort_by_color(shuffle_cards):
    sort_cards = sorted(shuffle_cards, key=type_color)
    return sort_cards