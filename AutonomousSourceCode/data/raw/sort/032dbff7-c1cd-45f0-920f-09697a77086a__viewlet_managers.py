from zope.viewlet.manager import ViewletManagerBase
from zope.traversing.browser import absoluteURL



class QreatureMenuVM(ViewletManagerBase):
    def sort(self, viewlets):
        return sorted(viewlets)
    

    
class QreatureLeftSideBarVM(ViewletManagerBase):
    def sort(self, viewlets):
        return sorted(viewlets)
    
class QreatureRightSideBarVM(ViewletManagerBase):
    def sort(self, viewlets):
        return sorted(viewlets)