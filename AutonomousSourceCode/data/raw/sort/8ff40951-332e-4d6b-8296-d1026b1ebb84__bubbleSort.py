#!/usr/bin/python
# -*- coding: utf-8 -*-


def bubble(listToSort, length):
	for i in range(length-1):
		if listToSort[i] > listToSort[i+1]:
			tmp = listToSort[i]
			listToSort[i] = listToSort[i+1]
			listToSort[i+1] = tmp


def bubbleSort(listToSort):
	for i in range(len(listToSort),0,-1):
		bubble(listToSort, i)

	return listToSort



if __name__=="__main__":  
    listToSort = [2,7,3,8,5,1,0,5,8,16,39,1,3,23,12,34,82,6,2,8,55,5,20]
    
    sortedList = bubbleSort(listToSort)
    print sortedList