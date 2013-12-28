#!/usr/bin/env python

"""
Transitions and transversion.
  Given: two DNA strings s1 and s2 of equal length (at most 1 kbp).
  Return: the transition/transversion ratio R(s1, s2).

Sample dataset:
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
Sample output:
1.21428571429

Usage: tran <FILE | s1 s2>
       FILE must be a FASTA format file with at least two DNA strings.
"""

purines = "AG"
pyrimidines = "CT"

def are_type(base1, base2, base_type):
  return base1 in base_type and base2 in base_type

def tran(s1, s2):
  """
  Counts the number of transition and transversion mutations, and returns their
  ratio.
  """
  transitions = 0
  transversions = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      if are_type(s1[i], s2[i], purines) or are_type(s1[i], s2[i], pyrimidines):
        transitions += 1
      else:
        transversions += 1
  return transitions / transversions

if __name__ == "__main__":  
  import sys
  from fasta import fasta_list
  if len(sys.argv) == 2:
    try:
      s1, s2 = fasta_list(sys.argv[1])
    except IOError:
      print("Unable to open/read FASTA file", sys.argv[1])
      sys.exit(1)

  elif len(sys.argv) == 3:
    s1, s2 = sys.argv[1:]
  
  else:
    print(__doc__)
    sys.exit(1)

  print("{0:.11f}".format(tran(s1, s2)))
