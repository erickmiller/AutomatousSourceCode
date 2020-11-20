#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Apr 13, 2014 '
__author__= 'samuel'



#key subroutine
def merge(sorted_A, sorted_B):
    na = len(sorted_A)
    nb = len(sorted_B)
    idxa = 0
    idxb = 0
    rtn_list = []
    while True:
        if idxa == na:
            rtn_list = rtn_list + sorted_B[idxb:nb]
            break
        if idxb == nb:
            rtn_list = rtn_list + sorted_A[idxa:na]
            break
        if sorted_A[idxa] > sorted_B[idxb]:
            rtn_list.append(sorted_B[idxb])
            idxb += 1
        else:
            rtn_list.append(sorted_A[idxa])
            idxa += 1
    print '-> %s' % rtn_list
    return rtn_list


def merge_sort(A):
    n = len(A)
    if n == 1:
        return A
    sub_array_A = merge_sort(A[:n/2])
    sub_array_B = merge_sort(A[n/2:])
    print sub_array_A, sub_array_B,
    return merge(sub_array_A, sub_array_B)
    

def main():
    A = [1,2,3,9,6,10,5,31,8]
    B = merge_sort(A)
    print ''
    print B


if __name__ == '__main__':
    main()
