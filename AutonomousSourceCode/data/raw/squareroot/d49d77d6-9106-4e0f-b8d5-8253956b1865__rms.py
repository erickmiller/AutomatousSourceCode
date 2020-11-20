# -*- coding: utf-8 -*-

import math

def root_mean_square(x): # x is a list of values.
  """ Returns the root mean square (rms) given a list of values. """
  return math.sqrt(sum([i*i for i in x])/len(x))
  
def main(means):
  print "Input:", means
  means = map(float,means)
  print "root mean square = ", root_mean_square(means)

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2:
    sys.stderr.write('Usage: python %s mean1 mean2 mean3 ... \n' % sys.argv[0])
    sys.exit(1)
  main(sys.argv[1:])