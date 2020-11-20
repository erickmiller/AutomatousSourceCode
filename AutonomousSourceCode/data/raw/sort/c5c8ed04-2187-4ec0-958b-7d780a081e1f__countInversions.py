def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        leftHalf = array[:mid]
        rightHalf = array[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        return merge(leftHalf, rightHalf)

def merge(leftHalf, rightHalf):
    sortedArray = []
    while leftHalf is not None and rightHalf is not None:
        if leftHalf[0] <= rightHalf[0]:
            sortedArray.append(leftHalf.pop(0))
        else:
            sortedArray.append(rightHalf.pop(0))

    if leftHalf:
        sortedArray += leftHalf
    if rightHalf:
        sortedArray += rightHalf
    return sortedArray

array = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]

print(mergeSort(array))