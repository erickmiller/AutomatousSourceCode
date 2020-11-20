from hypothesis import given
from hypothesis.strategies import lists, integers, builds

def pop_least(list1,list2):
    """return the smaller element from one of two ordered lists, and remove it
    """
    if list1[0] <= list2[0]:
        return list1.pop(0)
    return list2.pop(0)

def merge_sorted_lists(sorted_list_1, sorted_list_2):
    """merge two ascending lists"""
    retlist = []
    while sorted_list_1 and sorted_list_2:
        retlist.append(pop_least(sorted_list_1,sorted_list_2))
    retlist.extend(sorted_list_1 if sorted_list_1 else sorted_list_2)
    return retlist

def sort_list(l):
    l.sort()
    return l
 
@given(builds(sort_list,lists(integers())),builds(sort_list,lists(integers())))
def test_merge(l1,l2):
    merged = merge_sorted_lists(list(l1),list(l2))
    expected = list(l1)
    expected.extend(l2)
    expected.sort()
    assert merged == expected
    
if __name__ == '__main__':
    test_merge()
