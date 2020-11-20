class Roots:

    # Finds the square root of a number using binary search.
    # number - int
    def square_root(self, number):
        left = 0
        right = number

        for a in range(100):
            middle = left + ((right - left) / 2)
            if middle ** 2 > number:
                right = middle
            else:
                left = middle

        return middle


def main():
    number = int(input())
    print('%.5f' % Roots().square_root(number))


if __name__ == '__main__':
    main()
