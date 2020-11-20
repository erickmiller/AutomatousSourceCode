def PIECE___root_mean_square_error():
    """PIECE___root_mean_square_error:

    ROOT_MEAN_SQUARE_ERROR = sum of squared differences between items in PREDICTED_OUTPUTS multi-dimensional
    array and TARGET_OUTPUTS multi-dimensional array, divided by the number of cases, then square-rooted
    """

    forwards = {'root_mean_square_error':
                    [lambda a0, a1: sqrt(((a1 - a0) ** 2).sum() / a0.shape[0]),
                     {'a0': 'target_outputs',
                      'a1': 'predicted_outputs'}]}

    backwards = {('DOVERD', 'root_mean_square_error', 'predicted_outputs'):
                     [lambda a0, a1, rmse: ((a1 - a0) / a0.shape[0]) / rmse,
                      {'a0': 'target_outputs',
                       'a1': 'predicted_outputs',
                       'rmse': 'root_mean_square_error'}]}

    return Piece(forwards, backwards)