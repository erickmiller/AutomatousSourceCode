def square_root_convergents():
    num = 3
    den = 2
    result = 0
    for i in range(1, 1001):
        num += 2 * den
        den = num - den
        if len(str(num)) > len(str(den)):
            result += 1
    return result
