'''
Arranged probability

due to double's precision, solving the equation by square root does not work

'quadratic diophantine equation' helps

756872327473
'''
def solution():
    b = 15
    n = 21
    target = 1000000000000

    while n < target:
        btemp = 3 * b + 2 * n - 2
        ntemp = 4 * b + 3 * n - 3

        b = btemp
        n = ntemp
    return b

if __name__ == '__main__':
    print('Result: ', solution())

