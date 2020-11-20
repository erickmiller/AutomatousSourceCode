import numpy as np


class BaseTargetTransform(object):

    @classmethod
    def transform(cls, y):
        return np.array(y)

    @classmethod
    def transform_back(cls, y):
        return np.array(y)


class SquareRootTargetTransform(BaseTargetTransform):

    @classmethod
    def transform(cls, y):
        y = np.clip(y, 0, np.inf)
        return np.array([np.sqrt(yy) for yy in y])

    @classmethod
    def transform_back(cls, y):
        return np.array([yy**2 for yy in y])


class LogTargetTransform(BaseTargetTransform):

    @classmethod
    def transform(cls, y):
        y = np.clip(y, 0, np.inf)
        return np.array([np.log(yy+1) for yy in y])

    @classmethod
    def transform_back(cls, y):
        return np.array([np.exp(yy)-1 for yy in y])


class TrimOutliersTargetTransform(BaseTargetTransform):

    @classmethod
    def transform(cls, y):
        return np.clip(y, 0, 20)

    @classmethod
    def transform_back(cls, y):
        return np.array(y)


class TrimOutliersSquareRootTargetTransform(BaseTargetTransform):

    @classmethod
    def transform(cls, y):
        y = np.clip(y, 0, 20)
        return SquareRootTargetTransform.transform(y)

    @classmethod
    def transform_back(cls, y):
        return SquareRootTargetTransform.transform_back(y)
