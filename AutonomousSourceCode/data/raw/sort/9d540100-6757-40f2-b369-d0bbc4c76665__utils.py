from django.utils.datastructures import SortedDict

def sort_dict(d, values=False):
    idx = values and 1 or 0
    return SortedDict(sorted(d.items(), cmp=lambda x,y: cmp(x[idx], y[idx])))
