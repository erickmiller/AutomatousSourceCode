import numpy as np 

def mse(actual, predicted):
	"""
	----------------------------------
	This function caluculates 
	mean square error between actual and predicted

	Takes: two lists / arrays
	Returns: mean square error
	----------------------------------
	"""

	return np.mean(np.abs(np.array(actual) - np.array(predicted)))


def rmse(actual, predicted):
	"""
	----------------------------------
	This function caluculates root
	mean square error between actual and predicted

	Takes: two lists / arrays
	Returns: root mean square error
	----------------------------------
	"""

	return np.sqrt(mse(actual, predicted))
	

def rmsle(actual, predicted):
	"""
	----------------------------------
	This function caluculates root mean
	square log error between actual and predicted

	Takes: two lists / arrays
	Returns: root mean square log error
	----------------------------------
	"""

	return np.sqrt(np.mean(np.power(np.log(np.array(actual) + 1) - np.log(np.array(predicted) + 1), 2)))
