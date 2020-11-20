def insenstiveSort(stringList):
    return sorted(stringList, key=str.lower)

def insenstiveSort(stringList):
    """ For both str and unicode"""
    return sorted(stringList, key=lambda x: x.lower())

print(insenstiveSort(['a', 'B', 'c']))
