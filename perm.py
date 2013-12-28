#!/usr/bin/env python

"""
Enumerating gene orders.
  Given: a positive integer n <= 7.
  Return: the total number of permutations of length n, followed by a list of
          all such permutations (in any order).

Sample dataset:
3
Sample output:
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

Usage: perm <FILE | n>
"""

def perm(nset, prefix = [], perms = []):
  """
  Recursively produces a list of all possible permutations of the given nset.
  """
  if len(nset) == 0:
    perms.append(prefix)
  else:
    for i in range(len(nset)):
      perm(nset[:i] + nset[i+1:], prefix + nset[i:i+1], perms)
  return perms

if __name__ == "__main__":  
  import sys
  if len(sys.argv) != 2:
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

  permutations = perm([i for i in range(1, n+1)])
  print(len(permutations))
  for permutation in permutations:
    print(' '.join(str(i) for i in permutation))
