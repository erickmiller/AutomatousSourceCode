__author__ = 'frank.ma'


class Sorting(object):

    def __init__(self,
                 lst: list):
        self.lst = lst
        self.lst_sorted = None

    def get_list(self):
        return self.lst

    def get_list_sorted(self):
        assert self.lst_sorted is not None, "input list is not sorted yet."
        return self.lst_sorted

    def __merge_sort_rec(self,
                         l: list):
        n = l.__len__()

        # base case
        if n <= 1:
            return l

        def __merge(lt: list,
                    rt: list):
            merged = []
            while lt and rt:
                if lt[0] < rt[0]:
                    merged.append(lt.pop(0))
                else:
                    merged.append(rt.pop(0))
            merged.extend(lt)
            merged.extend(rt)
            return merged

        # recursion case
        m = int(n / 2)

        left = self.__merge_sort_rec(l[:m])
        right = self.__merge_sort_rec(l[m:])

        return __merge(left, right)

    def merge_sort(self):
        self.lst_sorted = self.__merge_sort_rec(self.lst)