def sortNumber(n):
    list1 = []
    for i in xrange(len(str(n))):
        list1.append(str(n)[i])
    list1.sort()
    return "".join(list1)

def insert(n):
    sortedKey = sortNumber(n**3)
    if sortedKey in permDict:
        permDict[sortedKey].append(n)
    else:
        permDict[sortedKey] = [n]

def main():
    isFound = False
    counter = 1
    while not isFound:
        insert(counter)
        if len(permDict[sortNumber(counter**3)]) == 5:
            isFound = permDict[sortNumber(counter**3)][0] ** 3
        else:
            counter += 1
    print isFound

permDict = {}
main()
