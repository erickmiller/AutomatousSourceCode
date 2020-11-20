def get_array(file):
    return file.readline().split()


def bubble_sort(list):
    swaps = 0
    passes = 0
    sorted = False
    while sorted is False:
        sorted = True
        for i in range(0, (len(list)-1)):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swaps += 1
                sorted = False
        passes += 1
    return passes, swaps


file = open('data.txt', 'r')
size = int(file.readline())
print(bubble_sort([int(i) for i in get_array(file)]))
