from random import randint
def bozosort(list):
    toSort = list
    sorted = False
    runs = 0
    while sorted == False:
        sorted = True
        for i in range(0, len(toSort)-1):
            if toSort[i] > toSort[i+1]:
                sorted = False;
        if sorted == False:
            rand1 = randint(0, len(toSort)-1)
            rand2 = randint(0, len(toSort)-1)
            while rand1 == rand2:
                rand1 = randint(0, len(toSort)-1)
                rand2 = randint(0, len(toSort)-1)
            old_toSort1 = toSort[rand1]
            toSort[rand1] = toSort[rand2]
            toSort[rand2] = old_toSort1
            runs += 1
    return runs