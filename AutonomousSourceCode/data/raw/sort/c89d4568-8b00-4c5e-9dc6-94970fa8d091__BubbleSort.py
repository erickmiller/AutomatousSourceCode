# implementation of bubble sort algotithm
# time = O(n^2)
# space = O(1)

class BubbleSort:
    
    def sort(self, array):
        is_sorted = False
        arr_length = len(array)

        while not is_sorted:
            is_sorted = True
            for i in range(0, arr_length - 1):
                if array[i] > array[i+1]:
                    is_sorted = False
                    tmp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = tmp

        return array
