def isGreaterThan(valA, valB):
    return valA > valB

def sort_dict(d):
    sortedList = []
    for key in d:
        valueA = d[key]
        index = 0
        for (keyB, valueB) in sortedList:
            if isGreaterThan(valueA, valueB):
                break
            index = index + 1
        sortedList.insert(index, (key, valueA))
    return sortedList

if __name__ == "__main__":
    dictA = {3:1,2:2,1:3}
    expectedA = [(1,3),(2,2),(3,1)]
    print expectedA == sort_dict(dictA)

    dictB = {1:5,3:10,2:2,6:3,8:8}
    expectedB = [(3,10),(8,8),(1,5),(6,3),(2,2)]
    print expectedB == sort_dict(dictB)
