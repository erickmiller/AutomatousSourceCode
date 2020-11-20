# A simple implementation of bootstrap
import numpy as np
from numba import jit
@jit
def bootstrap(data, num_samples, statistics):
  data_size = len(data)
  values = []
  for i in range(num_samples):
    values.append(statistics(data[np.random.randint(0, data_size,  data_size)]))
  return values

def interval(bootstrap_data, alfa):
    sorted_values = np.array(bootstrap_data)
    sorted_values.sort()
    return (sorted_values[alfa/2.0*len(sorted_values)],
            sorted_values[(1.0 - alfa/2.0)*len(sorted_values)])
