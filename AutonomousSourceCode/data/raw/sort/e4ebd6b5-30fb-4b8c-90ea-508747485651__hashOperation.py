# this file contain multiple functions on python dictionary

def cumulativeInsert(hash, item, val):
    if item in hash:
        hash[item] += val
    else:
        hash[item] = val
    return hash


def count2Ratio(hash):
    N = sum(hash.values()) 
    hash = dict([(item, float("%.3f"%(hash[item]*100.0/N))) for item in hash])
    return N, hash


# create a 3-member tuple, key, value_in_sortedList, value_in_hash
def joint_with_sortedHash(sortedList, hash):
    tupleArr = []
    for item in sortedList:
        tuple = (item[0], item[1], hash[item[0]])
        tupleArr.append(tuple)

    return tupleArr


def sortHash(hash, sortField, reversedFlag):
    sortedList = sorted(hash.items(), key = lambda a:a[sortField], reverse=reversedFlag)
    return sortedList

def output_sortedHash(hash, sortField, reversedFlag):
    sortedList = sortHash(hash, sortField, reversedFlag)
    for item in sortedList:
        print item[0], "\t", item[1]

