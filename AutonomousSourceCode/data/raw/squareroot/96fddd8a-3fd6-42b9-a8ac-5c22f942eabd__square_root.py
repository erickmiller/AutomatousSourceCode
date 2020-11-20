def pseudo_bin_search(start, end, gap, number):
    left = start
    right = end
    curr = left + (right - left) / 2
    for i in range(120):

        doubled_curr = curr * curr
        if doubled_curr >= number and (curr - gap) * (curr - gap) <= number:
            return curr
        if doubled_curr < number:
            left = curr + gap
        if doubled_curr > number:
            right = curr - gap

        curr = left + (right - left) / 2


def bin_search(arr, number):
    left = 0
    right = len(arr) - 1
    curr = left + (right - left) // 2

    while left < right:
        if arr[curr + 1]**2 >= number and arr[curr - 1]**2 <= number:
            return arr[curr]

        if arr[curr]**2 < number:
            left = curr + 1

        if arr[curr]**2 > number:
            right = curr - 1

        curr = left + (right - left) // 2


def generate_range(number):
    left = 0
    right = number
    gap = 1
    return pseudo_bin_search(left, right, gap, number)


def square_root(number):
    max_item = generate_range(number)
    left = max_item - 1
    right = max_item + 1
    gap = 0.0000001

    return pseudo_bin_search(left, right, gap, number)

if __name__ == '__main__':
    number = int(input())
    # print("{}".format(square_root(number)))

    print("{0:.5f}".format(square_root(number)))
