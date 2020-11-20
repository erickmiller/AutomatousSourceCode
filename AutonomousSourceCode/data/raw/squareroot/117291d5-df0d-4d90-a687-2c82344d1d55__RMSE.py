#!/usr/bin/env python

# -------
# RMSE.py
# -------

def square_of_difference(x, y) :
    """
    Squares the differences between actual and predicted ratings
    x is one rating from the list of actual ratings
    y is one rating from the list of predicted ratings
    return the difference of each actual and predicted rating squared
    """
    rating_dict = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5}
    actual = rating_dict[x]
    pred = float(y)
    sd = (actual - pred) ** 2
    assert type(sd) is float
    return sd
  
def mean(a) :
    """
    Calculates the average of a list
    a is the list of ints or floats to average
    return the average of the numbers in the input list
    """
    assert type(a) is list
    m = sum(a) / len(a)
    assert 0 <= m <= 16
    return m
    
def rmse(a,p) :
    """
    Calculates the root mean square error between 2 lists
    a is the list of actual ratings
    p is the list of predicted ratings
    return root mean square error between the two input lists
    """
    assert type(a) is list
    assert type(p) is list
    assert len(a) == len(p) 
    r = mean(map(square_of_difference, a, p)) ** .5
    assert 0 <= r <= 4
    return r
