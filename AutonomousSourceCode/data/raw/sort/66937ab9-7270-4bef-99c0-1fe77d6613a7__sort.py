#! /usr/bin/python
import random
import time
import numpy
import sys

import quickSort
import selectionSort
import bubbleSort
import optBubbleSort
import insertionSort
import inplaceQuickSort
import utils
import heapSort
import inplaceSimpleQuickSort
import inplaceMidPivotQuickSort

def measureInline(sortObj):
	inputArr = utils.createInputArray(1000);
	startTime = time.time()
	outputArr = sortObj.sortList(inputArr)
	endTime = time.time()
	unsortedTime = (endTime - startTime)

	startTime = time.time()
	outputArr = sortObj.sortList(outputArr)
	endTime = time.time()
	sortedTime = endTime - startTime

	return (unsortedTime, sortedTime)

def measure(funcName, sortObj, count=10):
	unsortedTime = 0
	sortedTime = 0
	unsortedTimeArray = list()
	sortedTimeArray = list()
	for i in range(count):
		(unsortedTime, sortedTime) = measureInline(sortObj)
		unsortedTimeArray.append(unsortedTime)
		sortedTimeArray.append(sortedTime)
	averageUnsortTime = numpy.mean(unsortedTimeArray)
	averageSortTime = numpy.mean(sortedTimeArray)
	sortObj.setTime(averageUnsortTime, averageSortTime)
	print "Average Time taken by %s for unsorted is %2.3g" \
		%(funcName, averageUnsortTime) 
	print "Average Time taken by %s for sorted is %2.3g" \
		%(funcName, averageSortTime)

sortClassList = { 
	"InplaceMidPivotQuickSort" : inplaceMidPivotQuickSort.InplaceMidPivotQuickSort(),
	"InplaceSimpleQuickSort" : inplaceSimpleQuickSort.InplaceSimpleQuickSort(),
	"heapSort" : heapSort.HeapSort(),
	"InsertionSort": insertionSort.InsertionSort(),
	"BubbleSort": bubbleSort.BubbleSort(),
	"OptBubbleSort": optBubbleSort.OptBubbleSort(),
	"SimpleQuicksort": quickSort.QuickSort(),
	"InplaceQuicksort": inplaceQuickSort.InplaceQuickSort(),
	"selectionSort": selectionSort.SelectionSort()
}

def main():
	sys.setrecursionlimit(10000)
	for name in sortClassList:
		measure(name, sortClassList[name])

main()