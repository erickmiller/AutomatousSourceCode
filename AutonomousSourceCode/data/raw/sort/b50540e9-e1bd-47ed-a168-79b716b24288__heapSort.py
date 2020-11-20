import heapq


class MinHeap():
    def __init__(self):
        self.something = ''

    def extract_min(self):
        print('extract min')

    def insert(self):
        print('insert')

    def heapify(self):
        print('heapify')


def heap_sort(list):
    sorted_list = []
    min_heap = []
    for elem in list:
        heapq.heappush(min_heap, elem)
    for i in range(len(list)):
        sorted_list.append(heapq.heappop(min_heap))
    return sorted_list


print(heap_sort([10, 9, 8, 7, 6, 5, 4, 3]))
