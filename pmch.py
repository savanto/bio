#!/usr/bin/env python

"""
Perfect matchings and RNA secondary structures.
  Given: an RNA string s of length at most 80 bp having the same number of
         occurences of 'A' as 'U' and the same number of occurences of 'C' as
         'G'.
  Return: the total possible number of _perfect_ matchings of basepair edges
          in the bonding graph of s.

Sample dataset:
>Rosalind_23
AGCUAGUCAU
Sample output:
12

Usage: pmch <FILE1 | s1> [FILE2 | s2] [FILE3 | s3] ...
       FILEs must be in FASTA format.
"""

def pmch(s):
  """
  Returns the number of perfect matchings of basepair edges possible in the
  bonding graph of s.
  perfect matchings possible = (#gc/2)! * (#au/2)!
  """
  gc = 0
  au = 0
  for base in s:
    if base in "GC":
      gc += 1
    elif base in "AU":
      au += 1

  gc_fact = 1
  au_fact = 1
  for i in range(gc // 2, 1, -1):
    gc_fact *= i
  for i in range(au // 2, 1, -1):
    au_fact *= i

  return gc_fact * au_fact

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
    print(pmch(s))
