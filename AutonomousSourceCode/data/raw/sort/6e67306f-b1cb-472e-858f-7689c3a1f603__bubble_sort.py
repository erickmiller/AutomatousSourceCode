#07. 09. 2013
#Author : Joon Lim


# Bubble sort algorithm
A = [31, 41, 59, 26, 41, 58]


def bubble_sort(L):
    '''This is the bubble sort algorithm'''
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(L) - 1): #there are up to n-1 switches
            if L[i] > L[i+1]:
                sorted = False
                L[i], L[i+1] = L[i+1], L[i]
    return L



# TIP : more practical way using numpy
A = np.array([31, 41, 59, 26, 41, 58])

A.sort() # insertion sort - O(nlogn)
A.sort(kind='mergesort') # merge sort - O(nlogn)
