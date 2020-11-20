# examples
sort_dict({3:1,2:2,1:3}) == [(1,3),(2,2),(3,1)]
sort_dict({1:2,2:4,3:6}) == [(3,6),(2,4),(1,2)]

# my solution
# zip is unnecessary
def sort_dict(d):
    'return a sorted list of tuples from the dictionary'
    return sorted(zip(d.keys, d.values()), key=lambda t: t[1], reverse=True)

# others
def sort_dict(d):
    return sorted(d.items(), key=lambda t: t[1], reverse=True)

from operator import itemgetter
def sort_dict(d):
    return sorted(d.items(), key=itemgetter(1), reverse=True)
