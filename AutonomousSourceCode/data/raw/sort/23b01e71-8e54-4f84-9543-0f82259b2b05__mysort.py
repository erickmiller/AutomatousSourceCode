import copy

def my_min(l):
  if l == []:
      raise 'this is an empty list'
  else:
      min_elem  = l[0]
      for i in l:
          if min_elem > i:
              min_elem = i
  return min_elem


def my_reverse(l):
    if len(l) == 0:
        raise 999
    else:
        return l[::-1]


def select_sort(list):
    l = copy.deepcopy(list)
    if len(l) == 0:
        raise 999
    else:
        my_sorted = []
        for i in range(len(l)):
            my_sorted.append(my_min(l))
            l.remove(my_min(l))
    return my_sorted


def insert_sort(l):
    if len(l) == 0:
        raise 999
    else:
        my_sorted = [l[0]]
        for i in range(1, len(l)):
            for j in range(len(my_sorted)):
                if my_sorted[j] >= l[i]:
                    my_sorted.insert(j, l[i])
                    break
                elif j == len(my_sorted) - 1:
                    my_sorted.append(l[i])
    return my_sorted


def tear_list(sorted1, sorted2):
    ret_sort = []
    i = j = 0
    while i < len(sorted1) and j < len(sorted2):
        if sorted1[i] < sorted2[j]:
            ret_sort.append(sorted1[i])
            i += 1
        else:
            ret_sort.append(sorted2[j])
            j += 1
    while i < len(sorted1):
        ret_sort.append(sorted1[i])
        i += 1
    while j < len(sorted2):
        ret_sort.append(sorted2[j])
        j += 1
    return ret_sort



def add_up_sort(l):
    if len(l) == 0:
        raise  999
    elif len(l) == 1:
        return l
    else:
        sorted1 = add_up_sort(l[: len(l) / 2])
        sorted2 = add_up_sort(l[len(l) / 2 :])
    return tear_list(sorted1, sorted2)


l = [1, 5, 36, 67, 4, 7, 78, 100]
add_up_sort(l)


