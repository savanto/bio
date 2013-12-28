#!/usr/bin/env python

"""
Enumerating oriented gene orderings.
  Given: a positive integer n <= 6.
  Return: the total number of signed permutations of length n, followed by a
          list of all such permutations (you may list signed permutations in
          any order).

Sample dataset:
2
Sample output:
8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1

Usage: sign <FILE | n>
"""

from perm import perm

def mask(n, combo = [], masks = []):
  """
  Recursively creates sign masks to be applied to standard permutations to make
  signed permutations.
  """
  if len(combo) == n:
    masks.append(combo)
  else:
    mask(n, combo + [1], masks)
    mask(n, combo + [-1], masks)
  return masks

def sign(nset):
  """
  After creating sign masks and normal permutations of given set of elements,
  produces a list of signed permutations as a result of applying signed masks
  to the normal permutations.
  """
  masks = mask(len(nset))
  perms = perm(nset)
  signs = []
  for p in perms:
    for m in masks:
      signs.append([a * b for a, b in zip(p, m)])
  return signs

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  try:
    with open(sys.argv[1]) as f:
      n = int(f.readline().strip())
  except IOError:
    try:
      n = int(sys.argv[1])
    except ValueError:
      raise ValueError
  except ValueError:
    print("Invalid value for n given --", sys.argv[1])
    sys.exit(1)

  permutations = sign([i for i in range(1, n+1)])
  print(len(permutations))
  for permutation in permutations:
    print(' '.join(str(i) for i in permutation))
