# mdhandle,  http://github.com/dtlussier/mdhandle
# Copyright (c) 2008, Dan Lussier @ Oxford University, FBG Group
# Released under the GNU General Public License, v2
"""
Analyze fluctuations in time series stored in :class:`numpy.ndarray`.

"""

# TODO: Add function for square difference between two time series.

# -----------------------------------------------------------------------------

import sys

import numpy as np

# -----------------------------------------------------------------------------


def square_fluct(in1):
    """
    Calculates ``(in1 - <in1>)*(in1 - <in1>)``.

    ``<...>`` stands for the average over the whole vector.

    Parameters
    ----------
    in1: :class:`numpy.ndarray`
        (Nx1) NumPy array.

    Returns
    -------
    sq_fluct : :class:`numpy.ndarray`
    """

    sq_fluct = (in1 - in1.mean())**2
    return sq_fluct


def root_mean_square_fluct(in1):
    """
    Calculates mean squre fluctuation or root-mean-square (RMS) error.

    Parameters
    -----------
    in1 : :class:`numpy.ndarray`
        (Nx1) Numpy array

    Returns
    -------
    rms : :class:`numpy.ndarray`
        Mean square fluctuation.

    Notes
    -----

    RMS: Square-root of arithmetic mean of squares of original values.

    For an unbiased estimator, the RMSE is the square root of the variance,
    known as the standard error.

    References
    -----------
    * http://mathworld.wolfram.com/Root-Mean-Square.html
    * http://en.wikipedia.org/wiki/Root_mean_square_error

    """
    rms = np.sqrt(square_fluct(in1).sum() / in1.size)
    return rms


#=============================================================================


def main(argv=None):
    pass


if __name__ == "__main__":
    sys.exit(main())
