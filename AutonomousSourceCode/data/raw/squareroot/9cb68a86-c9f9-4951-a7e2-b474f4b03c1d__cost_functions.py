"""
a set of cost functions for Neural Network layers.
"""

import theano.tensor as T


def l1_norm(w):
    """
    Returns L1 norm of the given matrix (w).
    L1 norm is simply sum of a matrix elements.

    @input: w, a theano shared variable.
    @output: L1 norm of w
    """

    return abs(w).sum()


def l2_norm(w):
    """
    Returns L2 norm of the given matrix (w).
    L2 norm of a matrix is simply square root of the sum of square of elements of the matrix.
    In an other word, it's length for a matrix.

    @input: w, a theano shared variable.
    @output: L2 norm of w
    """

    return T.sqrt((w ** 2).sum())


def l2_norm_sqr(w):
    """
    Returns square of L2 norm of the given matrix (w).
    square of L2 norm of a matrix is simply the sum of square of elements of the matrix.
       
    @input: w, a theano shared variable.
    @output: L2 norm of w
    """

    return (w ** 2).sum()

# TODO
# add contractive cost function.
