_funcName = None
import random
from . import sort

def testAll():
	global _funcName
	funcArr = [_testMergeSort, _testMergeSortLarge]
	for i, func in enumerate(funcArr):
		for j in range(10):
			succ = func()
			_funcName = func.__name__
			_print("test " + str(j+1) + " start")
			if succ:
				_print("test " + str(j+1) + " pass")
			else:
				_print("test " + str(j+1) + " failed")

def _testMergeSort():
	ar = [random.randint(-100, 100) for x in range(random.randint(1,50))]
	_print(ar)
	arSorted = sort.mergeSort(ar[:])
	_print(arSorted)
	if arSorted == sorted(ar):
		return True
	else:
		return False

def _testMergeSortLarge():
	ar = [random.randint(-100, 100) for x in range(100000)]
	arSorted = sort.mergeSort(ar[:])
	if arSorted == sorted(ar):
		return True
	else:
		return False

def _print(msg):
	print(_funcName, end=": ")
	print(msg)