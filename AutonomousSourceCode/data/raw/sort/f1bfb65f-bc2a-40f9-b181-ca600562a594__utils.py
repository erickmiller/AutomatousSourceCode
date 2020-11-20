import numpy as np

def argSort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)

def block(im, p, r = 7):
    return im[p[1]-r:p[1]+r,p[0]-r:p[0]+r,:]

def cond(arr, c):
  return arr[c.argsort()[len(c)-sum(c):]]
