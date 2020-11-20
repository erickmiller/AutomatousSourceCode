def square_root(number):
    left = 0
    right = number
    mid = left + (right - left) / 2.0
    while True:
        if mid**2 > number:
            right = mid
        if mid**2 < number:
            left = mid
        if abs(mid**2 - number) < 0.00001:
            break
        mid = left + (right - left) / 2.0
    return mid

def main():
    print(square_root(25))

if __name__ == '__main__':
    main()
