class QuickSort:

    def quick_sort(self, array):
        if len(array) < 1:
            return array
        else:
            less, more, equal = [], [], []
            pivot = array[0]
            for i in array:
                if i < pivot:
                    less.append(i)
                elif i > pivot:
                    more.append(i)
                else:
                    equal.append(i)
            less_sorted = self.quick_sort(less)
            more_sorted = self.quick_sort(more)
            return less_sorted + equal + more_sorted

if __name__ == '__main__':
    qs = QuickSort()
    array = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print(qs.quick_sort(array))