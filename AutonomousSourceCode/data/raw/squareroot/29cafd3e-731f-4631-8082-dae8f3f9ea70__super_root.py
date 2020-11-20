def super_root(number):
    divisor = 1
    hi = number + 0.001
    low = number - 0.001
    super_root = 1

    while True:
        current = super_root**super_root
        if low < current < hi:  # good to go!
            return super_root
        elif current > hi:      # time to backtrack
            divisor /= 2
            super_root -= divisor
        elif current < low:     # clearer than else?
            super_root += divisor

if __name__ == '__main__':
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
