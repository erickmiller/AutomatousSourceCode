import sys
import math
import time


def main():
    case_num = raw_input("Please input your cases:\n")
    for i in range(1, int(case_num) + 1):
        detect_case(i)


def detect_case(case):
    num_range = (sys.stdin.readline()).split('\n')[0]
    min = int(num_range.split(" ")[0])
    max = int(num_range.split(" ")[1])
    result = get_num(min, max)
    sys.stdout.write("\nCase #{}: {}\n".format(case, result))


def get_num(min, max):
    result = 0
    for i in range(min, max + 1):
        if is_par_square(i):
            result += 1
    return result


def is_par_square(number):
    if is_par(str(number)) and is_square(number):
        if is_par(str(int(math.sqrt(number)))):
            return True
    return False


def is_par(number):
    reversed_number = ""
    if 1 == len(number):
        return True
    else:
        for i in range(len(number) - 1, -1, -1):
            reversed_number += number[i]
        if number == reversed_number:
            return True
    return False


def is_square(number):
    square_root = str(math.sqrt(number)).split('.')[1]
    if 1 == len(square_root) and '0' == square_root:
        return True
    return False


if __name__ == "__main__":
    startTime = time.clock()
    main()
    sys.stdout.write("The running time is {}(s)\n".format(time.clock() - startTime))
