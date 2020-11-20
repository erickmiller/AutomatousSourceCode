#!/usr/bin/python

import random

def get_random_list(num=10):
    l = range(0, num)
    random.shuffle(l)
    return l

def is_sorted(l):
    for i in range(0, len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def quick_sort(nums=[]):
    quick_sort.cnum = 0
    quick_sort.swaps = 0
    def swap(l, i, j):
        if i == j:
            return
        temp = l[i]
        l[i] = l[j]
        l[j] = temp
        quick_sort.swaps +=1

    def sublist_sort(nums, a, b):
        if a >= b:
            return
        pivot = nums[b]
        i = a
        j = b-1
        while i<=j:
            while nums[i] < pivot:
                quick_sort.cnum +=1
                if i >= b:
                    break
                i += 1

            while nums[j] >= pivot:
                quick_sort.cnum +=1
                if j <= a:
                    break
                j -= 1
            if i<j:
                swap(nums, i, j)
                i += 1
                j -= 1
            else:
                break

        swap(nums, i, b)
        sublist_sort(nums, a, i-1)
        sublist_sort(nums, i+1, b)

    if len(nums) > 0:
        sublist_sort(nums, 0, len(nums)-1)

def quick_sort2(nums=[]):
    if len(nums) == 0:
        return []
    else:
        return quick_sort2([x for x in nums[1:] if x < nums[0]]) + [nums[0]] + quick_sort2([x for x in nums[1:] if x>=nums[0]])

if __name__ == '__main__':
    l = get_random_list(20)
    print l
    quick_sort(l)
    print l
    print "Sorted: %s, # comparisons: %d, # of swaps: %d" % (is_sorted(l), quick_sort.cnum, quick_sort.swaps)
