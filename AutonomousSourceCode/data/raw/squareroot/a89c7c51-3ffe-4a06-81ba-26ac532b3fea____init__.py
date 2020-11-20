__author__ = 'eric'

import numpy as np
import theano.tensor as T


def sigmoid(x):
    # return 1. / (1 + numpy.exp(-x))
    # but, overflow because of exp(-x)
    # transfer to tanh, works!
    return 0.5 * (1 + np.tanh(x / 2))


def sigmoid_T(x):
    return 0.5 * (1 + T.tanh(x / 2))


def inv_sigmoid(x):
    """
    inverse sigmoid
    """
    return np.log(x / (1. - x))


def inv_sigmoid_T(x):
    return T.log(x / (1. - x))


def RMSE(a, b):
    """
    Root Mean Square Error
    """
    return np.sqrt(np.sum(np.square(a - b), axis=1))


def RMSE_T(a, b):
    return T.sqrt(T.sum(T.square(a - b), axis=1))


if __name__ == "__main__":
    lb = np.array([1, 2, 3, 4, 5])
    print sigmoid(lb)