from decimal import *

__author__ = 'Eddie'

START_NUM = 00000000
END_NUM = 99999999
REQUIRED_ROOT_LIST = [1, 4, 7, 9]

def solve():
    for num in range(START_NUM, END_NUM+1):
        super_number = generate_super_number(num)
        print "Checking {0}, {1}".format(str(num).zfill(8), super_number)
        if is_perfect_square(super_number):
            return int(Decimal(super_number).sqrt())

    return None

def get_digital_root(num):
    """
    Gets the digital sum of a number
    :param num: Int
    :return: Int
    """
    while len(str(num)) > 1:
        r = 0
        while num:
            r, num = r + num % 10, num / 10
        num = r

    return num

def generate_super_number(num):
    """
    Shuffles num in between 1234567890 to generate the special number to check.
    :param num: Int
    :return: Int
    """
    new_num = int('0'.join(list(str(num).zfill(8))) + '000')
    new_num += 1020304050607080900
    return int(new_num)

def is_perfect_square(num):
    """
    Determines whether or not a number is a perfect square. Checks using its digital root first to
    rule out impossible choices. We know that for a number to be a square number, its digital root
    must be 1, 4, 7, or 9
    :param num: Int
    :return: Boolean
    """
    digital_root = get_digital_root(num)
    if digital_root not in REQUIRED_ROOT_LIST:
        return False

    # Satisfies the square digital root test, now actually check if its a perfect square.
    if Decimal(num).sqrt() % 1 == 0:
        return True

    return False

if __name__ == "__main__":
    answer = solve()
    print "The answer is: {0}".format(answer)