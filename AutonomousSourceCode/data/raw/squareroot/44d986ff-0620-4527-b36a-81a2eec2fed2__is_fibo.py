import math

T = int(input())


def is_square(n):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return True
    else:
        return False


for i in range(T):
    N = int(input())
    pair = [5 * N ** 2 + 4, 5 * N ** 2 - 4]
    if is_square(pair[0]) or is_square(pair[1]):
        print("IsFibo")
    else:
        print("IsNotFibo")