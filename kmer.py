#!/usr/bin/env python

"""
K-mer composition.
  Given: a DNA string s in FASTA format (having length at most 100 kbp).
  Return: the 4-mer composition of s.

Sample dataset:
>Rosalind_6431
CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG
Sample output:
4 1 4 3 0 1 1 5 1 3 1 2 2 1 2 0 1 1 3 1 2 1 3 1 1 1 1 2 2 5 1 3 0 2 2 1 1 1 1 3 1 0 0 1 5 5 1 5 0 2 0 2 1 2 1 1 1 2 0 1 0 0 1 1 3 2 1 0 3 2 3 0 0 2 0 8 0 0 1 0 2 1 3 0 0 0 1 4 3 2 1 1 3 1 2 1 3 1 2 1 2 1 1 1 2 3 2 1 1 0 1 1 3 2 1 2 6 2 1 1 1 2 3 3 3 2 3 0 3 2 1 1 0 0 1 4 3 0 1 5 0 2 0 1 2 1 3 0 1 2 2 1 1 0 3 0 0 4 5 0 3 0 2 1 1 3 0 3 2 2 1 1 0 2 1 0 2 2 1 2 0 2 2 5 2 2 1 1 2 1 2 2 2 2 1 1 3 4 0 2 1 1 0 1 2 2 1 1 1 5 2 0 3 2 1 1 2 2 3 0 3 0 1 3 1 2 3 0 2 1 2 2 1 2 3 0 1 2 3 1 1 3 1 0 1 1 3 0 2 1 2 2 0 2 1 1

Usage: kmer <FILE | s> [k]
       FILE is a FASTA format file with a DNA string.
       k defaults to 4 if not specified.
"""

from lexf import lexf

dna_bases = ['A', 'C', 'G', 'T']

def kmer(s, k):
  """
  Uses lexf to create all possible k-mers from dna_bases. Counts the frequency
  of each k-mer in the DNA string s, and returns the dict with frequency counts.
  """
  composition = {}
  for kmer in lexf(dna_bases, k):
    composition[kmer] = 0
  for i in range(len(s) - k + 1):
    composition[s[i:i+k]] += 1
  return composition

if __name__ == "__main__":  
  import sys
  from fasta import fasta_string
  if len(sys.argv) in (2, 3):
    try:
      s = fasta_string(sys.argv[1])
    except IOError:
      s = sys.argv[1]

    k = 4
    if len(sys.argv) == 3:
      try:
        k = int(sys.argv[2])
      except ValueError:
        print("Invalid input for k --", sys.argv[2])
        print("Using default k = 4")

  else:
    print(__doc__)
    sys.exit(1)

  print(' '.join(str(freq) for kmer, freq in sorted(kmer(s, k).items())))
