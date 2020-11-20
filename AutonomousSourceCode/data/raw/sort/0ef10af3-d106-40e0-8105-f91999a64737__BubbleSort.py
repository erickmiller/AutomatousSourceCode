__author__ = 'dihnatsyeu'

def bublesort (ListToSort):

    lenght = len(ListToSort)
    sorted = False
    for j in range(0, lenght-1):
        for i in range(0, lenght-j-1):
            if ListToSort[i] > ListToSort[i+1]:
               temp = ListToSort[i]
               ListToSort[i] = ListToSort[i+1]
               ListToSort[i+1] = temp
               sorted = True
            if sorted == False: break

    return ListToSort

print bublesort([24,1,34,3,72,5,21])