from pl.edu.agh.neural.learning.backpropagation.error.RootMeanSquare import RootMeanSquare

class ErrorUtil(object):
    ROOT_MEAN_SQUARE = RootMeanSquare.NAME

    REGISTERED_FUNCTIONS = {
        ROOT_MEAN_SQUARE: RootMeanSquare
    }

    @staticmethod
    def registered_factors():
        return ErrorUtil.REGISTERED_FUNCTIONS.keys()

    @staticmethod
    def get_factor(name):
        if name == ErrorUtil.ROOT_MEAN_SQUARE:
            return ErrorUtil.REGISTERED_FUNCTIONS[name]

    @staticmethod
    def default_factor():
        return ErrorUtil.ROOT_MEAN_SQUARE
