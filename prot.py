#!/usr/bin/env python

"""
Translating RNA into protein.
  Given: an RNA string s corresponding to a strand of mRNA (of length at
         most 10kbp).
  Return: the protein string encoded by s.

Sample dataset:
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
Sample output:
MAMAPRTEINSTRING

Usage: prot <FILE1 | s1> [FILE2 | s2] ...
"""

rna_codons = { "UUU": 'F',   "CUU": 'L',   "AUU": 'I',   "GUU": 'V',
               "UUC": 'F',   "CUC": 'L',   "AUC": 'I',   "GUC": 'V',
               "UUA": 'L',   "CUA": 'L',   "AUA": 'I',   "GUA": 'V',
               "UUG": 'L',   "CUG": 'L',   "AUG": 'M',   "GUG": 'V',
               "UCU": 'S',   "CCU": 'P',   "ACU": 'T',   "GCU": 'A',
               "UCC": 'S',   "CCC": 'P',   "ACC": 'T',   "GCC": 'A',
               "UCA": 'S',   "CCA": 'P',   "ACA": 'T',   "GCA": 'A',
               "UCG": 'S',   "CCG": 'P',   "ACG": 'T',   "GCG": 'A',
               "UAU": 'Y',   "CAU": 'H',   "AAU": 'N',   "GAU": 'D',
               "UAC": 'Y',   "CAC": 'H',   "AAC": 'N',   "GAC": 'D',
               "UAA": '',    "CAA": 'Q',   "AAA": 'K',   "GAA": 'E',
               "UAG": '',    "CAG": 'Q',   "AAG": 'K',   "GAG": 'E',
               "UGU": 'C',   "CGU": 'R',   "AGU": 'S',   "GGU": 'G',
               "UGC": 'C',   "CGC": 'R',   "AGC": 'S',   "GGC": 'G',
               "UGA": '',    "CGA": 'R',   "AGA": 'R',   "GGA": 'G',
               "UGG": 'W',   "CGG": 'R',   "AGG": 'R',   "GGG": 'G' }

def prot(s):
  """
  Translates a given mRNA string s into a protein string from a lookup
  table of RNA codons. If a codon is not found in table, a '?' is output.
  """
  protein = []
  for i in range(3, len(s) + 1, 3):
    protein.append(rna_codons.get(s[i-3:i], '?'))
  return protein

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  for filename in sys.argv[1:]:
    try:
      with open(filename) as f:
        s = f.read().strip()
    except IOError:
      s = filename
    print(''.join(prot(s)))

