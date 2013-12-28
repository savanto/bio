#!/usr/bin/env python

"""
Creating a distance matrix.
  Given: a collection of n (n <= 10) DNA strings s1, ..., sn of equal length
         (at most 1 kbp). Strings are given in FASTA format.
  Return: The matrix D corresponding to the p-distance dp on the given strings.
          As always, note that your answer is allowed an absolute error of 0.001.

Sample dataset:
>Rosalind_9499
TTTCCATTTA
>Rosalind_0942
GATTCATTTC
>Rosalind_6568
TTTCCATTTT
>Rosalind_1833
GTTCCATTTA
Sample output:
0.00000 0.40000 0.10000 0.10000
0.40000 0.00000 0.40000 0.30000
0.10000 0.40000 0.00000 0.20000
0.10000 0.30000 0.20000 0.00000

Usage: pdst <FILE | s1 s2 [s3 [s4 [ ...]]]>
       FILE must be in FASTA format
"""

from hamm import hamm

def pdst(dna_strings):
  """
  Compute the p-distance (dp) matrix D from the list of dna_strings using
  Hamming distance.
  """
  num_strings = len(dna_strings)
  string_length = len(dna_strings[0])
  # Initilize D to zeros
  D = [ [0 for i in range(num_strings)] for i in range(num_strings) ]
  for i in range(num_strings):
    for j in range(num_strings):
      D[i][j] = hamm(dna_strings[i], dna_strings[j]) / string_length
  return D

if __name__ == "__main__":  
  import sys
  from fasta import fasta_list
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  elif len(sys.argv) == 2:
    try:
      dna_strings = fasta_list(sys.argv[1])
    except IOError:
      print("Unable to open/read FASTA file", sys.argv[1])
      sys.exit(1)

  else:
    dna_strings = sys.argv[1:]

  for row in pdst(dna_strings):
    print(' '.join("{0:.5f}".format(i) for i in row))
