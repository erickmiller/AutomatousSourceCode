#!/usr/bin/python
import sys
import operator 

def primes (q):
  return (i for i in xrange(2,q) if i not in [j*k for j in xrange(2,i/2+1) for k in xrange(2,min(j+1,i/j+1))])

def gap (p, q):
  sorted_primes = list(set(primes(q)) - set(primes(p)))
  sorted_primes.sort()
  n = len(sorted_primes)
  a = []
  high_gaps = {}
  low_gaps = {}
  gapped_primes = {}
  for i in range(n):
    if(0 < i < n - 1):
      gap_l = sorted_primes[i] - sorted_primes[i-1]
      gap_h = sorted_primes[i+1] - sorted_primes[i]
      high_gaps[sorted_primes[i]] = gap_h
      low_gaps[sorted_primes[i]] = gap_l
      print "p(" + str(i) + "): \t" + str(sorted_primes[i]) + " \t" + str(gap_l) +  " " + str(gap_h) + " " + str((gap_h + gap_l)/2)
  gaps_descending = list(reversed(sorted(a)))
  sorted_hg = sorted(high_gaps.items(), key=operator.itemgetter(1), reverse=True)
  sorted_lg = sorted(low_gaps.items(), key=operator.itemgetter(1), reverse=True)
  for i in range (n-2):
    index_l = [y[0] for y in sorted_lg].index(sorted_primes[i+1])
    index_h = [x[0] for x in sorted_hg].index(sorted_primes[i+1])
    sum_indices = index_l + index_h
    #print str(sum_indices) + " " + str(sorted_primes[i+1]) + " " + str(sorted_hg[index_h]) + " " + str(sorted_lg[index_l])
    gapped_primes[sum_indices] = sorted_primes[i+1]
 #for i in range(n-2):
  #  sum_indices = sorted_hg[sorted_primes[i]].
  sorted_primes_gapped = sorted(gapped_primes.items(), key=operator.itemgetter(0))
  for i in range(10):
    gap_l = low_gaps[sorted_primes_gapped[i][1]]
    gap_h = high_gaps[sorted_primes_gapped[i][1]]
    gap_m = (gap_l + gap_h)/2
    print str(sorted_primes_gapped[i]) + " " + str(gap_h) + " " + str(gap_l) + " " + str(gap_m)




def main(argv):
  if len(sys.argv) < 3:
    print "please try with 2 numbers, p < q"
    sys.exit(2)
  else:
    gap (int(argv[1]), int(argv[2]))

if __name__ == "__main__":
  main(sys.argv)
