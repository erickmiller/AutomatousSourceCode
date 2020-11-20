__author__ = 'Aneesh Garg'

from Heap import Heap

class HeapSort:

    def sort(self, data):
        print("Heapsort of size "+ str(len(data)))
        if len(data) > 0:
            heap = Heap(data)
            #print("Heap ===> " + heap.printHeap())
            sortedData = []
            while heap.size > 0:
                sortedData.append(heap.removeMin())
            return sortedData
        else:
            return data
