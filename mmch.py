#!/usr/bin/env python

"""
Maximum matchings and RNA secondary structures.
  Given: an RNA string s of length at most 100.
  Return: the total possible number of matchings of basepair edges in the
          bonding graph of s.

Sample dataset:
>Rosalind_92
AUGCUUC
Sample output:
6

Usage: mmch <FILE1 | s1> [FILE2 | s2] [FILE3 | s3] ...
       FILEs must be in FASTA format.
"""

def mmch(s):
  """
  Counts G, C, A, U content of s and returns the total possible number of
  maximum matchings of basepair edges.
  """
  # Count base pairs
  count = {'A': 0, 'C': 0, 'G': 0, 'U': 0}
  for base in s:
    count[base] += 1
  a = list(range(count['A'], 0, -1))
  u = list(range(count['U'], 0, -1))
  au = a[:len(u)] if len(u) < len(a) else u[:len(a)]
  g = list(range(count['G'], 0, -1))
  c = list(range(count['C'], 0, -1))
  gc = g[:len(c)] if len(c) < len(g) else c[:len(g)]
  au_fact = 1
  gc_fact = 1
  for i in au:
    au_fact *= i
  for i in gc:
    gc_fact *= i
  return au_fact * gc_fact


if __name__ == "__main__":  
  import sys
  from fasta import fasta_list
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  rna_strings = []
  for filename in sys.argv[1:]:
    try:
      rna_strings += fasta_list(filename)
    except IOError:
      rna_strings.append(filename)
  for s in rna_strings:
    print(mmch(s))
