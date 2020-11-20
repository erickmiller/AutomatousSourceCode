
import numpy as np

class RegressionMetrics:
    
    def __init__(self):
        pass
    
    def rmse(self, yPred, yTrue):
        """Finds the root mean square error """
        return np.sqrt(np.mean(np.power((yPred - yTrue), 2)))
    
    def mae(self, yPred, yTrue):
        """Finds the mean absolute error"""
        return np.mean(np.fabs(yPred - yTrue))
    
    
if __name__ =="__main__":
    pass