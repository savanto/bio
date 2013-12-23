#!/usr/bin/env python

"""
Finding a motif in DNA.
  Given: two DNA strings s and t (each of length at most 1 kbp).
  Return: all locations of t as a substring of s.

Sample dataset:
GATATATGCATATACTT
ATAT
Sample output:
2 4 10

Usage: subs <FILE1> [FILE2] ...
"""

def match(s, t, i):
  for j in range(len(t)):
    if t[j] != s[i+j]:
      return False
  return True

def subs(s, t):
  """
  Traverse DNA string s, finding all locations where t is a substring of s
  NB: returned positions are zero-indexed, but Rosalind requires them to
  be 1-indexed.
  """
  positions = []
  len_s = len(s)
  len_t = len(t)
  if len_t <= len_s:
    for i in range(len_s - len_t):
      if match(s, t, i):
        positions.append(i)
  return positions

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  for filename in sys.argv[1:]:
    try:
      with open(filename) as f:
        s = f.readline().strip()
        t = f.readline().strip()
    except IOError:
      print("Skipping file", filename, ": unable to open/read file.")
      continue
    print(' '.join(str(i+1) for i in subs(s, t)))
