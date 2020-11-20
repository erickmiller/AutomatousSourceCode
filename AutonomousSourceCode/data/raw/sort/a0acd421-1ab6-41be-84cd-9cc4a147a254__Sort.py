class Sort():
    def __init__(self):
        pass
    
    ##Bubble sort. Not efficient at all. Relies on the ">" operator
    ##To perform sorting
    #@param toBeSorted      List that we wish to be sorted. 
    def bubble_sort(self, toBeSorted):
        for e in toBeSorted:
            for i in range(len(toBeSorted) - 1):
                if (toBeSorted[i] > toBeSorted[i+1]):
                    temp = toBeSorted[i]
                    toBeSorted[i] = toBeSorted[i+1]
                    toBeSorted[i + 1] = temp
        return toBeSorted
    
    ##Merge sort 
    #@param toBeSorted      List that we wish to be sorted.
    def merge_sort(self, toBeSorted):
        if (len(toBeSorted) == 1):
            return toBeSorted

        middle = len(toBeSorted) / 2
        
        left = toBeSorted[0:middle]
        right = toBeSorted[middle: len(toBeSorted)]
        
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        result = self.__merge(left, right)
        
        return result
    
    ##Used by the merge sort public function
    def __merge(self, left, right):
        result = []
        while (len(left) > 0 or len(right) > 0):
            if (len(left) > 0 and len(right) > 0):
                if (left[0] <= right[0]):
                    result.append(left[0])
                    left = left[1:len(left)]
                else:
                    result.append(right[0])
                    right = right[1:len(right)]
            elif (len(left) > 0):
                result.append(left[0])
                left = left[1:len(left)]
            else:
                result.append(right[0])
                right = right[1:len(right)]
        return result
            