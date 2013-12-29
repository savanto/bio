#!/usr/bin/env python

"""
Partial permutations.
  Given: positive integers n and k such that 100 >= n > 0 and 10 >= k > 0.
  Return: the total number of partial permutations P(n, k), modulo 1000000.

Sample dataset:
21 7
Sample output:
51200

Usage: pper <FILE | n k>
"""

def pper(n, k):
  """
  Calculates partial permutations P(n, k) = n! / (n-k)! % 1000000
  """
  partial_perm = 1
  for i in range(n, n-k, -1):
    partial_perm = (partial_perm * i) % 1000000
  return partial_perm


if __name__ == "__main__":  
  import sys
  if len(sys.argv) == 2:
    try:
      with open(sys.argv[1]) as f:
        n, k = (int(i) for i in f.readline().strip().split())
    except ValueError:
      print("Invalid values for n and k in file", sys.argv[1])
      sys.exit(1)
    except IOError:
      print("Unable to open/read file", sys.argv[1])
      sys.exit(1)

  elif len(sys.argv) == 3:
    try:
      n, k = (int(i) for i in sys.argv[1:3])
    except ValueError:
      print("Invalid values for n and k --", ' '.join(sys.argv[1:3]))
      sys.exit(1)

  else:
    print(__doc__)
    sys.exit(1)

  print(pper(n, k))
