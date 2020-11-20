#Find square root of an input

def sqrt(num):
    if num < 0:
        return ValueError
    if num == 1:
        return 1
    low = 0
    high = 1+(num/2)

    while low+1 < high:
        mid = low+(high-low)/2
        square = mid ** 2
        if square == num:
            return mid
        elif square < num:
            low = mid
        elif square > num:
            high = mid
    return low
