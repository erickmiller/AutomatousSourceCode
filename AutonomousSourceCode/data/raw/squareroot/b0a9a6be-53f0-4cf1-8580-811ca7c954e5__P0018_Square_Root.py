__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def square_root(number: int, n_step: int) -> float:
    r = 1

    for _ in range(n_step):
        d = number / r
        r = (r + d) / 2

    return r


def main() -> int:
    n = int(input())
    results = [''] * n

    for i in range(n):
        (number, steps) = map(int, input().split())
        results[i] = str(square_root(number, steps))

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())