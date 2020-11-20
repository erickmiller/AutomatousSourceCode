def main(list_to_sort):
  sublist1, sublist2 = split_list(list_to_sort)
  if len(sublist1) > 2:
    main(sublist1)
  if len(sublist2) > 2:


def split_list(list_to_sort):
  list_halfway_point = len(list_to_sort)/2
  sublist1 = list_to_sort[0:list_halfway_point]
  sublist2 = list_to_sort[list_halfway_point:]
  if len(sublist1) > 1:
    split_list(sublist1)
  if len(sublist2) > 1:
    split_list(sublist2)
  return sublist1, sublist2


def reconstruction(list1, list2):
  sorted_list = []
  for item1 in list1:
    for item2 in list2:
      if item1 < item2:
        sorted_list.append(item1)
      else:
        sorted_list.append(item2)






def single_item_comparison(small_list):
  if num2 < num1:
    return [num2, num1]
  else:
    return [num1, num2]
