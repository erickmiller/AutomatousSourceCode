#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import*
from decimal import Decimal
import numpy as np
from sklearn import preprocessing

def to_nomalized(a):
    return preprocessing.normalize(a)

def to_float(a):
    for i in range(len(a)):
        a[i] = float(a[i])
    return a
def dis_to_sim(d):
    return 1/(1+d)

def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

def manhattan_distance(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))

def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)

def minkowski_distance(x,y,p_value):
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)

def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)

def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)


def loge(n,li,ls):
    if fabs(li-ls) <= 0.000001:
        return (li+ls)/2.0
    if (exp(li)-n)*(exp((li+ls)/2.0)-n) < 0:
        return loge(n,li,(li+ls)/2.0)
    else:
        return loge(n,(li+ls)/2.0,ls)
def ln(n):
    if n == 0 or n < 0:
        return "Math Domain Error"
    if n == 1:
        return 0
    if n > 0 and n < 1:
        return loge(n,0,-n-80)
    else:
        return loge(n,0,n)
def bhatta_distance(hist1, hist2, num):
    h1 = np.average(hist1)
    h2 = np.average(hist2)

    dis = 0;
    for i in range(num):
        dis += sqrt( hist1[i] * hist2[i])
    if h1 != h1:
        dis = sqrt( 1 - ( 1 / sqrt(h1*h2*num*num) ) * dis)
    return dis
