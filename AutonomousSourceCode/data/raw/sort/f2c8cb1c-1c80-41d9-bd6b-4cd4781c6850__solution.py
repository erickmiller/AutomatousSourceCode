def sort_a_list(l):
   x = sorted
   return x(l, reverse=True)
from operator import attrgetter, itemgetter
getcount = itemgetter(0)
def sort_by_mark(my_class):
    i = sorted
    return i(my_class,  key=getcount, reverse=True)
getcounts = itemgetter(1)
def sort_by_name(my_class):
    i = sorted
    return i(my_class,  key=getcounts)
