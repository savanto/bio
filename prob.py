#!/usr/bin/env python

"""
Introduction to random strings.
  Given: a DNA string s of length at most 100 bp and an array A containing at
         most 20 numbers between 0 and 1.
  Return: an array B having the same length as A in which B[k] represents the
          common logarithm of the probability that a random string constructed
          with GC-content found in A[k] will match s exactly.

Sample dataset:
ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783
Sample output:
-5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009

Usage: prob <FILE1> [FILE2] [FILE3] ...
"""

import math

def prob(s, A):
  """
  Calculates the common logarithm of the probability of producing string s
  if GC-content is given in array A.
  log(x * y) = log(x) + log(y)
  """
  B = []
  for gc in A:
    at = 1 - gc
    p = 0
    for base in s:
      if base in "GC":
        p += math.log(gc / 2, 10)
      elif base in "AT":
        p += math.log(at / 2, 10)

    B.append(p)

  return B

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  for filename in sys.argv[1:]:
    try:
      with open(filename) as f:
        s = f.readline().strip()
        A = list(float(i) for i in f.readline().strip().split())
    except ValueError:
      print("Skipping file", filename, ": invalid input for A.", filename)
      continue
    except IOError:
      print("Skipping file", filename, ": unable to open/read file.", filename)
      continue

    print(' '.join("{0:.3f}".format(i) for i in prob(s, A)))
