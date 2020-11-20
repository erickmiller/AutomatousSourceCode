def read_in_file():
    filename = 'IntegerArray.txt'
    f = open(filename, 'r')
    numbers = []
    for entry in f:
        numbers.append(int(entry))
    f.close()
    return numbers


def use_example():
    return [8, 4, 3, 2, 3, 5, 1, 0, 10]


def sort_and_count(ar):
    if len(ar) == 1:
        return 0, ar
    else:
        ct_left, left = sort_and_count(ar[0:len(ar) / 2])
        ct_right, right = sort_and_count(ar[len(ar) / 2::])
        # print left + right
        ar_sorted, ct_split = count_split(left, right)
        # print ar_sorted
        # print ct_left, ct_right, ct_split
        return ct_left + ct_right + ct_split, ar_sorted


def count_split(left, right):
    ar_sorted = []
    i = j = 0
    count = 0
    while i < len(left) and j < len(right):
        if(left[i] > right[j]):
            count += len(left) - i
            ar_sorted.append(right[j])
            j += 1
        else:
            ar_sorted.append(left[i])
            i += 1

    if j == len(right):
        ar_sorted += left[i:]
    else:
        ar_sorted += right[j:]

    return ar_sorted, count


if __name__ == "__main__":
    result, _ = sort_and_count(read_in_file())
    print result
