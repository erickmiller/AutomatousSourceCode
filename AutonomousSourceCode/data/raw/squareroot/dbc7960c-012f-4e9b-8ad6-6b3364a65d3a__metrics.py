import numpy as np

# Calculate Root Mean Square Logarithmic Error for difference of target-values and the
# corresponding predictions
def rmsle(target, prediction):
    squared_diff = np.power(np.log1p(prediction) - np.log1p(target), 2)
    return np.sqrt(squared_diff.mean())