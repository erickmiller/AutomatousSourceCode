def merger_sort_recursive(input):
    if (len(input) <= 1):
        return input

    middle = len(input) / 2
    leftSortedPart = merger_sort_recursive(input[:middle])
    rightSortedPart = merger_sort_recursive(input[middle:])

    return merge(leftSortedPart, rightSortedPart)


def merge(input1, input2):
    output = [None] * (len(input1) + len(input2))
    k = 0
    i = 0
    j = 0
    while (i < len(input1) and j < len(input2)):
        if (input1[i] < input2[j]):
            output[k] = input1[i]
            i+=1
        else:
            output[k] = input2[j]
            j+=1
        k+=1

    if (i == len(input1)):
        while (j < len(input2)):
            output[k] = input2[j]
            j+=1
            k+=1
    else:
        while (i < len(input1)):
            output[k] = input1[i]
            i+=1
            k+=1
    return output

def merge_sort(input):
    return merger_sort_recursive(input)


print merge_sort([56,12,48,99,1,60])

