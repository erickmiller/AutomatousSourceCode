# -*- coding:utf-8 -*-

from heapq import heappush, heappop


def heapSort(array):
    """
    Running Time
    ------------
    :rtype : object
    :param array: 
    Average: O(n*log(n))
    Best: O(n*log(n))
    Worst: O(n*log(n))
    """
    
    
    # 'Equivalent to sorted(iterable)'
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]
 





    
    return sortedArray

if __name__ == '__main__':
    import random
    array = [random.randint(1, 2 ** 32) for f in xrange(10000)]
    sortedArray = heap_sort(array)
    print sortedArray
    print max(sortedArray)
    print min(sortedArray)
