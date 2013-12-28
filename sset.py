#!/usr/bin/env python

"""
Counting subsets.
  Given: a positive integer n (n <= 1000)
  Return: the total number of subsets of {1, 2, ..., n} modulo 1000000.

Sample dataset:
3
Sample output:
8

Usage: sset <FILE1 | n1> [FILE2 | n2] [FILE3 | n3] ...
       FILEs must contain a single integer n.
"""

def sset(n):
  """
  Produces the total number of subsets of the set {1, 2, ..., n} mod 1000000.
  Since the number of subsets of any set is always 2^|set|, this function
  simply calculates 2^n % 1000000.
  """
  subsets = 1
  for i in range(n):
    subsets = (subsets * 2) % 1000000
  return subsets

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  for filename in sys.argv[1:]:
    try:
      with open(filename) as f:
        n = int(f.readline().strip())
    except ValueError:
      print("Skipping file", filename,": invalid input for n.")
      continue
    except IOError:
      try:
        n = int(filename)
      except ValueError:
        print("Skipping invalid input for n --", filename)
        continue

    print(sset(n))
