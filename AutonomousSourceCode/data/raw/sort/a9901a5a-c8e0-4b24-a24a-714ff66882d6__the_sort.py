#!/usr/bin/python
#encoding=utf-8

'''
DSU模式, 这是一个通用的方法, 通过创建一个辅助的列表, 将问题转化为列表的排序，
从而可以利用默认的快速的 sort 方法
'''
# 不区分大小写对字符串列表排序 
def case_insensitive_sort(string_list):
    auxliliary_list = [ (x.lower(), x) for x in string_list ]
    auxliliary_list.sort()
    return [ x[1] for x in auxliliary_list ]
def case_insensitive_sort_another(string_list):
    return sorted(string_list, key=str.lower)
    # 对于 unicode 字符串 sorted(string_list, key = unicode.lower)
    # 同时适应普通字符串和Unicode字符串 
    # import string
    # sorted(string_list, key = stirng.lower) 
    # 或是 sorted(string_list, key = lambda s: s.lower())
# 根据对象的某个属性来排序
def sort_by_attr(seq, attr):
    # 引入索引 i 保证相同属性下保持原有的相对位置
    intermd = [ (gettart(x, attr), i, x) for i, x in enumerate(seq) ]
    intermd.sort()
    return [ x[-1] for x in intermd ]
# sorted 保证如果传入可选参数key，列表的元素永远不会被直接比较
# 所以不需要如上例中加入i
import operator
def sort_by_attr_another(seq, attr):
    return sorted(seq, key = operator.attrgetter(attr))
def sort_by_attr_replace(lst, attr):
    lst[:] = sort_by_attr(lst, attr)

# 根据字符串中内嵌的数字排序
import re
def get_number(s):
    re_digit = re.compile(r'(\d+)')
    pieces = re_digit.split(s)
    pieces[1::2] = map(int, pieces[1::2])
    return pieces[1::2]
def sort_strings_with_numbers(alist):
    anx = [ (get_number(s), s) for s in alist ]
    anx.sort()
    return [ s for __, s in anx ]
def sort_strings_with_numbers_another(alist):
    return sorted(alist, key=get_number)
if __name__ == '__main__':
    alist = ['file1.txt', 'file3.txt', 'file11.txt', 'file21.txt']
    print sort_strings_with_numbers(alist)
    print ' '.join(sort_strings_with_numbers_another(alist))
