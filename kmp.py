#!/usr/bin/env python

"""
Speeding up motif finding.
  Given: a DNA string s (of length at most 100 kbp) in FASTA format.
  Return: the failure array of s.

Sample dataset:
>Rosalind_87
CAGCATGGTATCACAGCAGAG
Sample output:
0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0

Usage: kmp <FILE1 | s2> [FILE2 | s2] ...
       FILEs must be in FASTA format.
"""

def kmp(s):
  """
  Produce a failure array (KMP partial match table) for given string s.
  Algorithm taken from
  https://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm
  """
  P = [0]
  pos = 1
  cnd = 0
  while pos < len(s):
    # first case: the substring continues
    if s[pos] == s[cnd]:
      cnd += 1
      P.append(cnd)
      pos += 1
    # second case: it doesn't, but we can fall back
    elif cnd > 0:
      cnd = P[cnd-1]
    # third case: no candidates (cnd = 0)
    else:
      P.append(0)
      pos += 1

  return P



if __name__ == "__main__":  
  import sys
  from fasta import fasta_list
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  dna_strings = []
  for filename in sys.argv[1:]:
    try:
      with open(filename) as f:
        dna_strings += fasta_list(filename)
    except IOError:
      dna_strings.append(filename)

  for s in dna_strings:
    print(' '.join(str(i) for i in kmp(s)))
