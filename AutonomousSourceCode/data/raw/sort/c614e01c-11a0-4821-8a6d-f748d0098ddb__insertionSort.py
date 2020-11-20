#!/usr/bin/python
# -*- coding: utf-8 -*-


def insertionSort(listToSort):
	for i in range(1,len(listToSort)):
		
		curVal = listToSort[i]
		pos = i

		while pos > 0 and listToSort[pos-1]>curVal:
			listToSort[pos] = listToSort[pos-1]
			pos = pos-1


		listToSort[pos] = curVal


	return listToSort




if __name__=="__main__":  
    listToSort = [2,7,3,8,5,1,0,5,8,16,39,1,3,23,12,34,82,6,2,8,55,5,20]
    
    sortedList = insertionSort(listToSort)
    print sortedList