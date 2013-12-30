#!/usr/bin/env python

"""
Counting phylogenetic ancestors.
  Given: a positive integer n (3 <= n <= 10000).
  Return: the number of internal nodes of any unrooted binary tree having
          n leaves.

Sample dataset:
4
Sample output:
2

Usage: inod <FILE | n> [FILE | n] [FILE | n] ...
"""

def inod(n):
  """
  Returns the number of internal nodes on any unrooted binary tree having n
  leaves (always n - 2).
  """
  return n - 2

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
      print("Skipping file", filename, ": invalid value for n.")
      continue
    except IOError:
      try:
        n = int(filename)
      except ValueError:
        print("Skipping invalid n value --", filename)
        continue

    print(inod(n))
