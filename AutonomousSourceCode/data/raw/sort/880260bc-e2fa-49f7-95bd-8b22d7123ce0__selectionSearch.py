__author__ = 'bruno'
import algorithms.sort.selectionSort as SelectionSort


def search(array, k):
    sorted_array = SelectionSort.sort(array)
    return sorted_array[k]