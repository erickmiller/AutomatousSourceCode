# $Id$

class ContentViewletManager(object):
    def sort(self, viewlets):
        return sorted(viewlets, lambda x, y: cmp(x[0], y[0]))
