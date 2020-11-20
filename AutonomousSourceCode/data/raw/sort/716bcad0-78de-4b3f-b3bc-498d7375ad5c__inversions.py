def merge(xs1, xs2):
    i = 0
    j = 0
    sorted_xs = []
    inversions = 0
    for k in range(len(xs1) + len(xs2)):
        if xs1[i] < xs2[j]:
            sorted_xs.append(xs1[i])
            i += 1
            if i == len(xs1):
                sorted_xs += (xs2[j:])
                return sorted_xs, inversions
        else:
            sorted_xs.append(xs2[j])
            j += 1
            inversions += len(xs1) - i
            if j == len(xs2):
                sorted_xs += (xs1[i:])
                return sorted_xs, inversions
    return sorted_xs, inversions


def sort_count_inversions(xs):
    if len(xs) == 1:
        return xs, 0
    mid = len(xs) / 2
    xs1 = xs[0:mid]
    xs2 = xs[mid:len(xs)]
    sorted_xs1, inversions1 = sort_count_inversions(xs1)
    sorted_xs2, inversions2 = sort_count_inversions(xs2)
    sorted_xs, inversions_merged = merge(sorted_xs1, sorted_xs2)
    return sorted_xs, inversions1 + inversions2 + inversions_merged


contents = file.read(file('integerArray.txt'))
numbers = contents.split('\r\n')
del numbers[-1]
numbers = map(lambda x: int(x), numbers)
print sort_count_inversions(numbers)[1]