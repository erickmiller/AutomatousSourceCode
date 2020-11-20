import random

def sort(array):
    #implement your sort here
    print(array)
    print('using built in sort to check if array is sorted ')
    print(sorted(array))

    return array

def initArray(array):
    # use your loop to initialize the array with random integers here


    return array


def main():
    array = [0, 5, 1]
    print(array)
    array = initArray(array)
    print(array)
    array = sort(array)
    print(array)


main()
