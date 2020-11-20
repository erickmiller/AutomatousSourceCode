from math import sqrt
from numpy import *
from utils.tools import convert2matrix

def root_mean_square(features, values, w, f=None):
    size = len(features[0])
    if f == None:
        v = dot(features, w) - values
    else:
        v = f(dot(features, w)) - values
    return sqrt(dot(v, v) / size)


