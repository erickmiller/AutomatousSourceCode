def bubble_sort(l):
  is_sorted = False

  counter = 0
  while is_sorted == False:
    is_sorted = True

    for i in range(len(l) - 1):    # go through each except last
      num1, num2 = l[i], l[i+1]
      if num1 > num2:              # if you have to switch,
        is_sorted = False          # it's not sorted
        l[i], l[i+1] = num2, num1  # switch the numbers
  return l

print bubble_sort([6, 5, 3, 1, 8, 7, 2, 4])