def mySort(list):
    sorted = []
    smallest = 0
    while len(list) > 0:
        smallest = min(list)
        sorted.append(smallest)
        list.remove(smallest)    
    return sorted



##### If list is SORTED in INCREASING ORDER - these algorithms can be used to search ###

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


## or (I PREFER THIS ONE!!) ##

def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False

## or (recursively) ##

def search3(L, e):
    if L == []:
        return False
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)
