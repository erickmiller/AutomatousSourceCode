# -*- coding: utf-8 -*-

from operator import itemgetter

class Sorter(object):
	@staticmethod
	def sort_by_year(moviedata):
		sortedlist = sorted(moviedata, key=itemgetter('Year'))
		return sortedlist