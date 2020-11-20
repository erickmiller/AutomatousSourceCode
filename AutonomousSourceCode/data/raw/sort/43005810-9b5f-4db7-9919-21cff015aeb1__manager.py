from zope.viewlet.manager import ViewletManagerBase

class SortingViewletManager(ViewletManagerBase):

    def sort(self, viewlets):
        return sorted(viewlets)