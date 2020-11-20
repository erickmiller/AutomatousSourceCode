def square_root(number):
    if number < 0.0:
        return -1

    if number == 0.0 or number == 1.0:
        return number

    precision = 0.00001
    start = 0
    end = number

    if number < 1.0:
        end = 1

    while end - start > precision:
        mid_point = make_mid_point(start, end)
        current_square = mid_point * mid_point
        if current_square == number:
            return print("{0:.5f}".format(mid_point))
        if current_square < number:
            start = mid_point
        else:
            end = mid_point

    print("{0:.5f}".format(make_mid_point(start, end)))


def make_mid_point(start, end):
    return start + (end - start) / 2


def main():
    number = int(input())
    square_root(number)


if __name__ == '__main__':
    main()
