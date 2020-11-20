import sys


def simple_sort(numbers):
    sorted_numbers = list()
    for number in numbers:
        sorted_numbers.append(float(number))
    sorted_numbers.sort()
    return sorted_numbers

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test:
        continue

    # 'test' represents the test case, do something with it
    sorted_numbers = simple_sort(test.strip().split(' '))
    output = str()
    for number in sorted_numbers:
        output += '{:.3f}'.format(number) + ' '
    output = output.strip()
    print(output)

test_cases.close()
