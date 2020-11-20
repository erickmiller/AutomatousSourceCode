def radix_sort(data, max_digit, digit=1):
  if digit > max_digit:
    return data
  else:
    sorted_list = []
    radix_list = [(i % 10**digit) // (10**(digit-1)) for i in data]
    for d in range(10):
      for i in range(len(data)):
        if radix_list[i] == d:
          sorted_list.append(data[i])
    return radix_sort(sorted_list, max_digit, digit=digit+1)

def sort(data):
  max_digit = max([len(str(i)) for i in data])
  return radix_sort(data, max_digit)
