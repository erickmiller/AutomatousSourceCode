"""
Write a program that sorts its command line arguments.
"""
#!/usr/bin/env python3
import sys

def sortThis(lis):
	lis.sort()
	return lis

argLis = sys.argv[1:]
fmt = ("%20s: %s")
print(fmt % ("Arguments", argLis))

sortedArgs = sortThis(argLis)
print(fmt % ("Sorted arguments:", sortedArgs))
