from random import randint

def randArray():
    array = []

    for i in range(0, 10):
        randnum = randint(1, 100)
        array.append(randnum)
    return array

def insertionSort(array):

    for key in range(1, len(array)):
        current = array[key]
        indx = key - 1
        while indx >= 0 and array[indx] > current:
            array[indx+1] = array[indx]
            indx -= 1
        array[indx+1] = current
    return array

array = randArray()
print(array)

sorted = insertionSort(array)
print("sorted")
print(sorted)