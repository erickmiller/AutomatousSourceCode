#!/usr/bin/python
# -*- coding: utf-8 -*-


def selectionSort(listToSort):

	for i in range(len(listToSort)-1,0,-1):
		maxPos = 0
		for j in range(1, i+1):
			if listToSort[j] > listToSort[maxPos]:
				maxPos = j

		tmp = listToSort[i]
		listToSort[i] = listToSort[maxPos]
		listToSort[maxPos] = tmp

	return listToSort





if __name__=="__main__":  
    listToSort = [2,7,3,8,5,1,0,5,8,16,39,1,3,23,12,34,82,6,2,8,55,5,20]
    
    sortedList = selectionSort(listToSort)
    print sortedList