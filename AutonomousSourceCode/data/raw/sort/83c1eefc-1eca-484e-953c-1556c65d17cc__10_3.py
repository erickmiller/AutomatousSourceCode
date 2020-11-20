def is_sorted(ser):
    ser1=ser[:]
    ser.sort()
    if ser==ser1:
        return True
    else:
        return False

s=['a','t','c']
print(is_sorted(s))
