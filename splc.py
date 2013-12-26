#!/usr/bin/env python

"""
RNA splicing.
  Given: a DNA string s (of length at most 1 kbp) and a collection of substrings
         of s acting as introns. All strings in FASTA format.
  Return: a protein string resulting from transcribing and translating the exons
          of s.

Sample dataset:
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCG
TGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
Sample output:
MVYIADKQHVASREAYGHMFKVCA

Usage: splc <FILE>
"""

from orf import dna_codons, start_codon

def splc(dna_strings):
  """
  Given a list of DNA strings, with the string in the first position being the 
  whole gene and subsequent strings being introns, this function will remove
  the introns and output a protein sequence translated from the remaining DNA
  string.
  """
  dna = dna_strings[0]
  for i in range(1, len(dna_strings)):
    dna = ''.join(dna.split(dna_strings[i]))

  i = 0
  codon = dna[i:i+3]
  while codon != start_codon:
    i += 1
    codon = dna[i:i+3]
    if len(codon) != 3:
    # No start codon found in entire dna string => not a valid protein
      return None

  # Codon is now a valid start codon, begin translation
  j = i
  protein = []
  try:
    while dna_codons[codon] != "Stop":
      protein.append(dna_codons[codon])
      j += 3
      codon = dna[j:j+3]
  except KeyError:
    # Not a valid codon => not a valid protein
    return None

  return ''.join(protein)

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  try:
    with open(sys.argv[1]) as fasta:
      fasta.readline().strip()
      dna_strings = []
      s = ""
      for line in fasta.readlines():
        if line[0] == '>':
          dna_strings.append(s)
          s = ""
        else:
          s += line.strip()
      dna_strings.append(s)
  except IOError:
    print("Unable to open/read file", sys.argv[1])
    sys.exit(1)
  print(splc(dna_strings))
