#!/usr/bin/env python

"""
Introduction to set operations.
  Given: a positive integer n (n <= 20000) and two subsets A and B of {1,2...n}.
  Return: six sets: union(A, B), intersection(A, B), A - B, B - A, Ac, Bc
          where set complements are taken with respect to {1, 2, ..., n}).

Sample dataset:
10
{1, 2, 3, 4, 5}
{2, 8, 5, 10}
Sample output:
{1, 2, 3, 4, 5, 8, 10}
{2, 5}
{1, 3, 4}
{8, 10}
{8, 9, 10, 6, 7}
{1, 3, 4, 6, 7, 9}

Usage: seto <FILE>
"""

def seto(n, A, B):
  """
  Produces required sets by using built-in set structure and methods.
  """
  return [A.union(B), A.intersection(B), A - B, B - A, n - A, n - B]

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  try:
    with open(sys.argv[1]) as f:
      n = set(range(1, int(f.readline().strip()) + 1))
      A = set(int(i) for i in f.readline().strip()[1:-1].split(", "))
      B = set(int(i) for i in f.readline().strip()[1:-1].split(", "))
  except ValueError:
    print("Invalid values in file", sys.argv[1])
    sys.exit(1)
  except IOError:
    print("Unable to open/read file", sys.argv[1])
    sys.exit(1)

  for s in seto(n, A, B):
    print(s)
