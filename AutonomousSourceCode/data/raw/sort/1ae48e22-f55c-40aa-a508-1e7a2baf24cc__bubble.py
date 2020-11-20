def sort(values):
    sorted = False
    while not sorted:
        sorted = True
        for x in range(len(values)-1):
            if values[x] > values[x+1]:
                sorted = False
                values[x], values[x+1] = values[x+1], values[x]

    return values
