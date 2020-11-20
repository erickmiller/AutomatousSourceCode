#!/usr/bin/python
import sys, random;

def merge_min_sort_rec(list, depth):
	if (len(list) <= 1):
		return list;
	print ' '*depth, "sorting list len", len(list);
	#print ' '*depth, list;
	divpt = len(list)/2;
	listx = list[0:divpt];
	listy = list[divpt:len(list)];
	sorted_lx = merge_min_sort_rec(listx, depth+1);
	sorted_ly = merge_min_sort_rec(listy, depth+1);
	sorted = [];
	x = 0;
	y = 0;
	while ((x < len(sorted_lx)) and \
	(y < len(sorted_ly))):
		if (sorted_lx[x][1] < sorted_ly[y][1]):
			sorted.append(sorted_lx[x]);
			x += 1;
		else:
			sorted.append(sorted_ly[y]);
			y += 1;
	sorted += sorted_lx[x:];
	sorted += sorted_ly[y:];
	print ' '*depth, "returning list", len(list);
	return sorted;	

def merge_min_sort(list):
	newlist = merge_min_sort_rec(list, 0);
	return newlist;

def choose_inequality(elemx, elemy, choice):
	if (not(choice)):
		if (elemx < elemy):
			return 1;
		else:
			return 0;
	else:
		if (elemx > elemy):
			return 1;
		else:
			return 0;

def merge_sort_rec(list, maxmin, display, depth):
	if (len(list) <= 1):
		if (display):
			print ' '*depth, list;
		return list;
	if (display):
		print ' '*depth, "sorting list len", len(list);
	#print ' '*depth, list;
	divpt = len(list)/2;
	listx = list[0:divpt];
	listy = list[divpt:len(list)];
	sorted_lx = merge_sort_rec(listx, maxmin, display, depth+1);
	sorted_ly = merge_sort_rec(listy, maxmin, display, depth+1);
	#print ' '*depth, sorted_lx, sorted_ly;
	sorted = [];
	x = 0;
	y = 0;
	while (choose_inequality(x, len(sorted_lx), 0) and \
	choose_inequality(y, len(sorted_ly), 0)):
		if (choose_inequality(sorted_lx[x][1], sorted_ly[y][1], maxmin)):
			sorted.append(sorted_lx[x]);
			x += 1;
		else:
			sorted.append(sorted_ly[y]);
			y += 1;
	sorted += sorted_lx[x:];
	sorted += sorted_ly[y:];
	if (display):
		print ' '*depth, "returning list", len(list);
	return sorted;	

def merge_sort(list, maxmin, display):
	newlist = merge_sort_rec(list, maxmin, display, 0);
	#print "REQUESTED SORTED LIST DONE!!!";
	return newlist;

#newlist = [];
#for i in range(0, 100, 1):
#	newlist.append((i, random.random() * 100));
#print newlist;

#print merge_min_sort(newlist);
	
