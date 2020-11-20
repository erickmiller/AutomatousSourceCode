def average(data):
    """finds average of a list of numbers"""
    return sum(data)/float(len(data))
def sum(data):
    """finds sum of a list of numbers"""
    total = 0
    for i in data:
        total+=i
    return total
def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss
def std-dev(data):
    """returns the standard deviation of a list of numbers"""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/n # the population variance
    return pvar**0.5
def mean(data):
    """alias for average. Both mean the same thing. (get it?)"""
    average(data)
def median(data):
    """returns the median of a set of data untested"""
    sortedList = sorted(data)
    lengthOfSortedList = len(sortedList)
    if lengthOfSortedList == 1:
        return sortedList[0]
    elif(lengthOfSortedList%2==0):
        return average(sortedList[(lengthOfSortedList/2)-1:lengthOfSortedList/2])
    else:
        return sortedList[(lengthOfSortedList/2)-1]
def quickSort(data):
    pass
def bubbleSort(data):
    length = len(data)
    sortedList = []
    while(len(sortedList)<length):
        currentHighest = data[0]
        for i in range(data):
            if(data[i]>currentHighest):
                currentHighest = data[i]
        sortedList.append(currentHighest)
    return reversed(sortedList)
        
def mergeSort(data):
    pass
