input = [1,5,3,7,6,2,9,3,5,6]
sorted = 0

def insSort(input, i, sorted):
    #exit function when sorted number = the length of the array
    if sorted == len(input):
        return input
    # compare value at location i with value in lower location
    elif input[i] >= input[i-1]:
        sorted += 1
        insSort(input, sorted, sorted)
    # if value at i is less than value below it, switch positions
    elif input[i] < input[i-1]:
        input[i], input[i-1] = input[i-1], input[i]

        insSort(input, i-1, sorted)

# takes array, value of i, highest i that is sorted
insSort(input, 1, 0)

print(input)
