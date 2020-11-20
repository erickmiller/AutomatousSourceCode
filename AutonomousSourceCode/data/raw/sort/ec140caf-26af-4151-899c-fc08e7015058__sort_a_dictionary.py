d = {3:'3', 1:'1', 2:'2', 0:'0'}
def sortedDictValues1(adict):
    items = adict.items()
    print items
##    [(0, '0'), (1, '1'), (2, '2'), (3, '3')]
    items.sort()
    return [value for key, value in items]

def sortedDictValues2(adict):
    keys = adict.keys()
    print keys
    keys.sort()
    return [dict[key] for key in keys]

def sortedDictValues3(adict):
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)

if __name__ == '__main__':
    print sortedDictValues3(d)
