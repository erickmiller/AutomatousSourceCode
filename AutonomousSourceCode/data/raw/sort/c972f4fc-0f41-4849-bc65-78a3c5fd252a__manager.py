# $Id: manager.py 69361 2008-08-01 15:10:53Z glenfant $

class ContentViewletManager(object):
    def sort(self, viewlets):
        return sorted(viewlets, lambda x, y: cmp(x[0], y[0]))
