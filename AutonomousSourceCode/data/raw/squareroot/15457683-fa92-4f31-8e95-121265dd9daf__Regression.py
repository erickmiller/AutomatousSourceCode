from __future__ import division
import numpy as np


class Regression(object):

    def __init__(self, d_mat, t_vec):
        """
        prepends 1's onto each row in the design matrix, and runs regressions,
        to find w.

        :param d_mat (Design matric):
        :param t_vec (Target vector):
        """

        self.d_mat = np.array(map(lambda x: [1] + x, d_mat))
        self.t_vec = np.array(t_vec)

    def predict(self, x):
        raise Exception('Not yet implemented')

    def root_mean_square(self):
        """
        Find the root-dimension_means-square error for the given regression
        :return:
        """
        N = len(self.d_mat)

        guess_sum = 0
        for i in range(N):
            guess_sum += (self.t_vec[i][0] - self.predict(i))**2

        return np.sqrt((1/N) * guess_sum)