#!/usr/bin/env python

"""
Comparing spectra with the spectral convolution.
  Given: two multisets of positive real numbers S1 and S2. The size of each
         multiset is at most 200.
  Return: the largest multiset of S1 (-) S2, as well as the absolute value of
          the number x maximizing (S1 (-) S2)(x) (you may return any such value
          if multiple solutions exist).

Sample dataset:
186.07931 287.12699 548.20532 580.18077 681.22845 706.27446 782.27613 968.35544 968.35544
101.04768 158.06914 202.09536 318.09979 419.14747 463.17369
Sample output:
3
85.03163

Usage: conv <FILE>
"""

def conv(S1, S2):
  """
  Calculates the Minkowski difference S1 (-) S2 and returns the largest
  multiplicity (ie. the largest number of times an element appears in the
  resulting set), as well as the value of that element.
  """
  multiplicity = {}
  for s1 in S1:
    for s2 in S2:
      diff = round(s1 - s2, 5)
      multiplicity[diff] = multiplicity.get(diff, 0) + 1
  m = max(multiplicity, key = multiplicity.get)
  return multiplicity[m], m


if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  try:
    with open(sys.argv[1]) as f:
      S1 = list(float(i) for i in f.readline().strip().split())
      S2 = list(float(i) for i in f.readline().strip().split())
  except ValueError:
    print("Invalid input for S1 and S2 in file", sys.argv[1])
    sys.exit(1)
  except IOError:
    print("Unable to open/read file", sys.argv[1])
    sys.exit(1)

  for v in conv(S1, S2):
    print(v)
