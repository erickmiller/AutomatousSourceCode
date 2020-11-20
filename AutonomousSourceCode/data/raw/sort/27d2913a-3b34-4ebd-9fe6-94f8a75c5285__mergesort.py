__author__ = "Antony Cherepanov"


def merge_sort(t_input):
    length = len(t_input)
    if 2 < length:
        half_length = length // 2
        left_half = t_input[:half_length]
        right_half = t_input[half_length:]
        sorted_left = merge_sort(left_half)
        sorted_right = merge_sort(right_half)
        i = 0
        j = 0
        result = list()
        for k in range(length):
            if len(sorted_left) <= i:
                result.extend(sorted_right[j:])
                break

            if len(sorted_right) <= j:
                result.extend(sorted_left[i:])
                break

            if sorted_left[i] < sorted_right[j]:
                result.append(sorted_left[i])
                i += 1
            else:
                result.append(sorted_right[j])
                j += 1

        return result

    else:
        if 1 == length:
            return t_input
        elif 2 == length:
            first = t_input[0]
            second = t_input[1]
            if first < second:
                return [first, second]
            else:
                return [second, first]