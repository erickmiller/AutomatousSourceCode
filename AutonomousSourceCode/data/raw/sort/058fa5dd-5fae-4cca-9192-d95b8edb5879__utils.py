
import operator

def sort_dict(data, reverse=False):
    if type(data) != dict:
        print 'Can only sort dicts'
        return data
    data_sorted = sorted(data.items(), key=operator.itemgetter(1), reverse=reverse)
    return data_sorted