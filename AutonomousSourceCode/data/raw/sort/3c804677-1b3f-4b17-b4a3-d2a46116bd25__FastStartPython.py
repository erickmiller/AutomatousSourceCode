import sys

"""
def main():
	print 'Hi)'
	print StringSortByLength()
"""

# Sort string by length	
def ssbl():
	a = ['aaaa','ss','q','ddd']
	return sorted(a, key = len)

if __name__ == '__main__':
 	print ssbl()