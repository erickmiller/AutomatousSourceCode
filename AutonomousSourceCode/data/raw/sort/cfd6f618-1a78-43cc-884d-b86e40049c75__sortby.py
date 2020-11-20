class SortBy(object):
    def __init__(self):
        pass

    def sort(self, list_):
        if len(list_) <= 10000:
            return sorted(list_)
        else:
            self.sort_in_chunks(list_)

    def sort_in_chunks(self, list_):
        """
        Sort the list by chunks as a parallel operation.

        """
        print self