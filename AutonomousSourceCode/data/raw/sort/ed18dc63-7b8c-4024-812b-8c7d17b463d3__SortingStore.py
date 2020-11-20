__author__ = 'Ronaldo'

import pandas as pd

class SortingStore:


    class LookupModes:
        EXACT_MATCH, EXACT_OR_GREATER = range(2)

    def __init__(self, dataframe):
        self.df = dataframe
        self.sorted_views = {}

    def set_sorted_view(self, sorted_view, key_column, ascending):
        self.df = sorted_view
        self.sorted_views = {key_column + `ascending`:sorted_view}

    def get_sorted_view(self, key_column, ascending):

        sorted_view = self.sorted_views.get(key_column + `ascending`)

        if not isinstance(sorted_view,pd.DataFrame):
            sorted_view = self.df.sort_index(by=[key_column], ascending=[0])
            self.sorted_views[key_column + `ascending`] = sorted_view

        return sorted_view


    def lookup(self, key_column, key_value, ascending=1, lookupMode = LookupModes.EXACT_MATCH):

        sorted_view = self.get_sorted_view(key_column, ascending)

        if lookupMode == self.LookupModes.EXACT_OR_GREATER:
            a = sorted_view[sorted_view[key_column]>=key_value]
            return a.irow(-1)
