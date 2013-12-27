#!/usr/bin/env python

"""
Finding a spliced motif.
  Given: two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
  Return: one collection of indices of s in which the symbols of t appear as a
          subsequence of s. If multiple solutions exist, return any one.

Sample dataset:
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA
Sample output:
3 8 10

Usage: sseq <FILE | s t>
"""

# TODO find ALL subsequences, not just the first one.
# Tried recursively, but for long sequences this is untenable.
# Try dynamic programming.

def sseq(s, t):
  locations = [];
  sub = 0
  len_t = len(t)
  for i in range(len(s)):
    if t[sub] == s[i]:
      locations.append(i)
      sub += 1
    if sub == len_t:
      return locations
  return []

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  elif len(sys.argv) < 3:
    try:
      with open(sys.argv[1]) as fasta:
        ID_s = fasta.readline().strip()
        line = fasta.readline().strip()
        s = ""
        while line[0] != '>':
          s += line
          line = fasta.readline().strip()
        ID_t = line
        line = fasta.readline().strip()
        t = ""
        while len(line) != 0:
          t += line
          line = fasta.readline().strip()
    except IOError:
      print("Unable to open/read FASTA file", sys.argv[1])
      sys.exit(1)
        
  else:
    s = sys.argv[1]
    t = sys.argv[2]
  print(' '.join(str(i+1) for i in sseq(s, t)))
