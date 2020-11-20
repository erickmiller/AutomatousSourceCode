import sys


class MergeSort:

    def __init__(self, array):
        self.array      = array
        self.inversions = 0

    def get_inversions(self):
        return self.inversions

    def sort(self):
        return self.merge_sort(self.array)

    def merge_sort(self, array):
        length = len(array)

        if length < 2:
            return array
        else:
            split_length = int(length / 2)
            array_x      = self.merge_sort(array[:split_length])
            array_y      = self.merge_sort(array[split_length:])
            sorted       = []

            length_x = len(array_x)
            index_x, index_y = 0, 0
            while len(sorted) < length:

                if array_x[index_x] > array_y[index_y]:
                    sorted.append(array_y[index_y])
                    index_y += 1
                    self.inversions += length_x - index_x
                else:
                    sorted.append(array_x[index_x])
                    index_x += 1

                if index_x == len(array_x):
                    sorted.extend(array_y[index_y:])

                if index_y == len(array_y):
                    sorted.extend(array_x[index_x:])

            return sorted


def main(argv):
    file = open(argv[0])
    unsorted_list = [int(element) for element in file.readlines()]
    file.close()

    sorter      = MergeSort(unsorted_list)
    sorted_list = sorter.sort()
    inversion   = sorter.get_inversions()
    print "file \'%s\' contained %s elements and was sorted with %s inversions" % (argv[0], len(sorted_list), inversions)


if __name__ == "__main__":
    main(sys.argv[1:])
