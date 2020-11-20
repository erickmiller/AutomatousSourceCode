import numpy as np
from math import sqrt

def loss(y_true, y_pred):
"""
Implementation of the Root Mean Square Percentage Error (RMSPE)
"""
	return sqrt(np.mean((y_true - y_pred)/y_true)**2)