#!/usr/bin/env python

import random

from collections import deque

from time import time

from utilities.KeyHeapq import KeyHeapq


class Strategy(object):
    """
    Class for the representation of a strategy.
    """
    def build_container(self):
        raise NotImplementedError()

    def insert(self, item, sorted_items):
        raise NotImplementedError()

    def pop(self, sorted_items):
        raise NotImplementedError()

    def sorted_iterator(self, sorted_items):
        raise NotImplementedError()

    def sort(self, sorted_items):
        raise NotImplementedError()

    def iterable(self, sorted_items):
        raise NotImplementedError()


class DepthStrategy(Strategy):
    """
    Class for the representation of a depth strategy.
    """
    def build_container(self):
        return []

    def insert(self, item, sorted_items):
        sorted_items.append(item)

    def pop(self, sorted_items):
        return sorted_items.pop()

    def sorted_iterator(self, sorted_items):
        return reversed(sorted_items)

    def sort(self, sorted_items):
        return list(sorted(sorted_items, key=lambda x: self.get_max_time(x.token), reverse=True))

    def iterable(self, sorted_items):
        return sorted_items.__iter__()

    def __str__(self):
        return 'depth'

    def __repr__(self):
        return str(self)

    def get_max_time(self, token):
        return max(token.wme_indexes)


class BreadthStrategy(Strategy):
    """
    Class for the representation of a breadth strategy.
    """
    def build_container(self):
        return deque()

    def insert(self, item, sorted_items):
        sorted_items.append(item)

    def pop(self, sorted_items):
        return sorted_items.popleft()

    def sorted_iterator(self, sorted_items):
        return sorted_items

    def sort(self, sorted_items):
        return deque(sorted(sorted_items, key=lambda x: self.get_max_time(x.token)))

    def iterable(self, sorted_items):
        return sorted_items.__iter__()

    def __str__(self):
        return 'breadth'

    def __repr__(self):
        return str(self)

    def get_max_time(self, token):
        return max(token.wme_indexes)


class RandomStrategy(Strategy):
    """
    Class for the representation of a random strategy.
    """
    def build_container(self):
        return []

    def insert(self, item, sorted_items):
        random.seed(time())
        index = 0 if not sorted_items else random.randrange(0, len(sorted_items))
        sorted_items.insert(index, item)

    def pop(self, sorted_items):
        return sorted_items.pop()

    def sorted_iterator(self, sorted_items):
        return sorted_items

    def sort(self, sorted_items):
        container = sorted_items if isinstance(sorted_items, list) else list(sorted_items)
        random.shuffle(container)
        return container

    def iterable(self, sorted_items):
        return sorted_items

    def __str__(self):
        return 'random'

    def __repr__(self):
        return str(self)


class SimplicityStrategy(Strategy):
    """
    Class for the representation of a simplicity strategy.
    """
    def build_container(self):
        return KeyHeapq(key=lambda x: x.complexity)

    def insert(self, item, sorted_items):
        sorted_items.heappush(item)

    def pop(self, sorted_items):
        return sorted_items.heappop()

    def sorted_iterator(self, sorted_items):
        return sorted_items

    def sort(self, sorted_items):
        return KeyHeapq(sorted_items, key=lambda x: x.complexity)

    def iterable(self, sorted_items):
        return sorted_items

    def __str__(self):
        return 'simplicity'

    def __repr__(self):
        return str(self)


class ComplexityStrategy(Strategy):
    """
    Class for the representation of a complexity strategy.
    """
    def build_container(self):
        return KeyHeapq(key=lambda x: -x.complexity)

    def insert(self, item, sorted_items):
        sorted_items.heappush(item)

    def pop(self, sorted_items):
        return sorted_items.heappop()

    def sorted_iterator(self, sorted_items):
        return sorted_items

    def sort(self, sorted_items):
        return KeyHeapq(sorted_items, key=lambda x: -x.complexity)

    def iterable(self, sorted_items):
        return sorted_items

    def __str__(self):
        return 'complexity'

    def __repr__(self):
        return str(self)


class NaiveLexStrategy(Strategy):
    """
    Class for the representation of a naive LEX strategy.
    """
    def build_container(self):
        return KeyHeapq(key=lambda x: self.__sort_wmes(x.token))

    def insert(self, item, sorted_items):
        sorted_items.heappush(item)

    def pop(self, sorted_items):
        return sorted_items.heappop()

    def sorted_iterator(self, sorted_items):
        return sorted_items

    def sort(self, sorted_items):
        return KeyHeapq(sorted_items, key=lambda x: self.__sort_wmes(x.token))

    def iterable(self, sorted_items):
        return sorted_items.__iter__()

    def __sort_wmes(self, token):
        return sorted(token.wme_indexes, reverse=True)

    def __str__(self):
        return 'lex'

    def __repr__(self):
        return str(self)


class NaiveMeaStrategy(Strategy):
    """
    Class for the representation of a naive MEA strategy.
    """
    def build_container(self):
        return KeyHeapq(key=lambda x: self.__sort_wmes(x.token))

    def insert(self, item, sorted_items):
        sorted_items.heappush(item)

    def pop(self, sorted_items):
        return sorted_items.heappop()

    def sorted_iterator(self, sorted_items):
        return sorted_items

    def sort(self, sorted_items):
        return KeyHeapq(sorted_items, key=lambda x: self.__sort_wmes(x.token))

    def iterable(self, sorted_items):
        return sorted_items.__iter__()

    def __sort_wmes(self, token):
        return token.wme_indexes[0]

    def __str__(self):
        return 'mea'

    def __repr__(self):
        return str(self)
