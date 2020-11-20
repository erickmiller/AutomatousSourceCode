"""
Bubble Sort
wiki: https://en.wikipedia.org/wiki/Bubble_sort
input: list of sortable objects
returns: new sorted array
"""
def bubble_sort(input):
    #Creates duplicate of input so input is not changed
    sorted = list(input)
    #Sets input_length equal to the length of input. 
    input_length = len(input)
    #Keeps track of whether or not a swap occured in a given iteration
    swap = True
    #Continues looping until a swap does not occur
    while swap:
        swap = False
        for i in range(input_length-1):
            #If element at index i is greater than element at index i+1 then swap elements
            if sorted[i] > sorted[i+1]:
                temp = sorted[i]
                sorted[i] = sorted[i+1]
                sorted[i+1] = temp
                swap = True
    return sorted

"""
Selection Sort
wiki: https://en.wikipedia.org/wiki/Selection_sort
input: list of sortable objects
returns: new sorted array
"""
def selection_sort(input):
    #Creates duplicate of input so input is not changed
    sorted = list(input)
    #Sets input_length equal to the length of input. 
    input_length = len(input)
    #Advance through the entire array
    for i in range(input_length):
        #Set min_index to index i
        min_index = i
        #Checks every element after index i to find smallest element
        for j in range(i,input_length):
            #If element at min_index index is smaller than element at index j then set min_index = j
            if sorted[min_index] > sorted[j]:
                min_index = j
        #If min_index is not index i then swap elements at those indexes
        if min_index != i:
            temp = sorted[i]
            sorted[i] = sorted[min_index]
            sorted[min_index] = temp
    return sorted