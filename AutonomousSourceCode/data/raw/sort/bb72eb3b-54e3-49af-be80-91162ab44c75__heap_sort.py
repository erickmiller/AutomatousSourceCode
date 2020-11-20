from heap import Heap


class HeapSort:

    def __init__(self, sequence, order=None):  # from min to max by default
        self.__heap = self.__make_heap(sequence, order)

    def h_sort(self):
        sorted_arr = []
        heap_size = self.__heap.size()
        while len(sorted_arr) < heap_size - 1:  # to remove None element on index #0
            sorted_arr.append(self.__heap.delete())
        return sorted_arr

    def __make_heap(self, sequence, order):
        heap = Heap(order)
        for element in sequence:
            heap.insert(element)
        return heap


def main():
    test_arr = [4, 13, 52, 7, 18, 3, 1, 6]
    sorter = HeapSort(test_arr)
    result = sorter.h_sort()
    print(result)


if __name__ == '__main__':
    main()
