__author__ = 'TeaEra'


def square_root(x):
    """
    Binary method;
    """
    if x == 0:
        return 0
    min_num = 1.0
    max_num = x
    half_num = 1.0
    while True:
        half_num = (min_num + max_num) / 2.0
        if half_num ** 2 == x or abs(half_num ** 2 - x) < 1e-5:
            return half_num
        elif half_num ** 2 < x:
            min_num = half_num
            max_num = max_num
        elif half_num ** 2 > x:
            min_num = 1.0
            max_num = half_num


def square_root_2(x):
    """
    Status: accepted;

    Newton-Raphson method
    """
    if x == 0:
        return 0
    k = 1.0
    while abs(k*k - x) > 1e-4:
        k = (k + x/k)/2.0
    return int(k)

if __name__ == "__main__":
    #
    print("---")
    print(square_root(9))
    #
    print("---")
    print(square_root(10))
    #
    print("---")
    print(square_root_2(9))
    #
    print("---")
    print(square_root_2(10))