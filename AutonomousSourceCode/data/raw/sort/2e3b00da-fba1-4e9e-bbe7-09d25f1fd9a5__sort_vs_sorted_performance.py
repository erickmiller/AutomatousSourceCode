import timeit

def test_sorted(filename):
    f_in = open(filename, 'r')
    unsorted_list = ' '.join(f_in).split()
    sorted_list = sorted(unsorted_list)
    f_in.close()
    return sorted_list

def test_sort(filename):
    f_in = open(filename, 'r')
    unsorted_list = ' '.join(f_in).split()
    unsorted_list.sort()
    f_in.close()
    return unsorted_list
    
def print_fastest(time1, name1, time2, name2):
    if (time1 < time2):
        amount_faster = time2 - time1
        print("The function using the {0} method executed {1:8f} seconds faster"
              .format(name1,amount_faster))
    else:
        amount_faster = time1 - time2
        print("The function using the {0} method executed {1:8f} seconds faster"
              .format(name2,amount_faster))

file = 'E:\\Python34\\Scripts\\unsorted_fruits.txt'      

sorted_timer = timeit.Timer(stmt="test_sorted(file)",
                             setup="from __main__ import test_sorted, file")
sort_timer = timeit.Timer(stmt="test_sort(file)",
                          setup="from __main__ import test_sort, file")

min_sorted_result = min(sorted_timer.repeat(3,100))
min_sort_result = min(sort_timer.repeat(3,100))

print("The argument for these functions during this test was '{0}'.\n"
      .format(file))
print('sorted: {0:8f}'.format(min_sorted_result))
print('sort: {0:8f}'.format(min_sort_result))


print_fastest(min_sorted_result, 'sorted', min_sort_result, 'sort')

