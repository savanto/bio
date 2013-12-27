#!/usr/bin/env python

"""
Counting point mutations
  Given: two DNA strings s and t of equal length (not exceeding 1kbp).
  Return: the Hamming distance dH(s, t)

Sample dataset:
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample output:
7

Usage: hamm <FILE | s t>
"""

def hamm(s, t):
  """
  Return the Hamming distance between two strings of equal length. Return -1 if
  strings are unequal.
  """
  length = len(s)
  if len(t) != length:
    return -1
  dh = 0
  for i in range(length):
    if s[i] != t[i]:
      dh += 1

  return dh

if __name__ == "__main__":  
  import sys

  if len(sys.argv) == 2:
    try:
      with open(sys.argv[1]) as f:
        s = f.readline().strip()
        t = f.readline().strip()
    except IOError:
      print("Unable to open/read file", sys.argv[1])
      sys.exit(1)

  elif len(sys.argv) == 3:
    s = sys.argv[1]
    t = sys.argv[2]
  else:
    print(__doc__)
    sys.exit(1)

  print(hamm(s, t))
