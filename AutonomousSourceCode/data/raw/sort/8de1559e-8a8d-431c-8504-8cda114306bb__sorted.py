#! /usr/bin/env python
# Filename: sorted

print sorted([2,134,5,657,78,34])
# reversed_cmp
def reversed_cmp(x, y):
	if x > y:
		return -1
	elif x < y:
		return 1
	return 0
print sorted([21,332,23,62,1,34,11,123], reversed_cmp)

#-------------------------------------------------------------

print sorted(['alice','Jacob','Bob','chenlina'])
# sort by first letter
def cmp_ignore_case(s1, s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 > u2:
		return 1
	elif u1 < u2:
		return -1
	return 0
print sorted(['alice','Jacob','Bob','chenlina'], cmp_ignore_case)