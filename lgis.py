#!/usr/bin/env python

"""
Longest increasing subsequence.

  Given: a positive integer n <= 10000 followed by a permutation p of length n.
  Return: a longest increasing subsequence of p, followed by a longest
          decreasing subsequence of p.

Sample dataset:
5
5 1 4 2 3
Sample output:
1 2 3
5 4 2

Usage: lgis <FILE>
       First line of FILE contains a single integer n.
       Subsequence lines of FILE contain space-delineated the permutation p.
"""

def lgis(p):
  """
  Finds longest increasing subsequence of p using dynamic programming.
  """
  l = []
  for i in range(len(p)):
    l.append(max([l[j] for j in range(i) if l[j][-1] < p[i]] or [[]], key=len)
        + [p[i]])
  return max(l, key=len)

def lgds(p):
  """
  Finds longest decreasing subsequence of p using dynamic programming.
  """
  l = []
  for i in range(len(p)):
    l.append(max([l[j] for j in range(i) if l[j][-1] > p[i]] or [[]], key=len)
        + [p[i]])
  return max(l, key=len)

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  try:
    with open(sys.argv[1]) as f:
      n = int(f.readline().strip())
      p = list(int(i) for i in f.read().split())
  except IOError:
    print("Could not open/read file", sys.argv[1])
    sys.exit(1)
  except ValueError:
    print("Invalid values for n or p in file", sys.argv[1])
    sys.exit(1)

# Longest increasing subsequence
print(' '.join(str(i) for i in lgis(p)))
# Longest decreasing subsequence
print(' '.join(str(i) for i in lgds(p)))
