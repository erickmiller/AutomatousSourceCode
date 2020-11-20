# -*- coding: utf-8 -*-


def sort_by_key(item_list, key):
    return sorted(item_list, key=lambda k: k[key])
