#!/usr/bin/env python

"""
Inferring mRNA from protein.
  Given: a protein string of length at most 1000 aa.
  Return: the total number of different RNA strings from which the protein
          could have been translated, modulo 1000000.

Sample dataset:
MA
Sample output:
12

Usage: mrna <FILE1 | p1> [FILE2 | p2] ...
"""

# Table that records the number of codons that can code for a given
#   amino acid.
num_aa_codons = { 'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4,
                  'H': 2, 'I': 3, 'K': 2, 'L': 6, 'M': 1, 'N': 2,
                  'P': 4, 'Q': 2, 'R': 6, 'S': 6, 'T': 4, 'V': 4,
                  'W': 1, 'Y': 2, "Stop": 3 }

def mrna(p):
  """
  The number of possible mRNA sequences that can make given protein p is equal
  to a1 * a2 * a3 * ... * aN where aN is the number of RNA codons that code for
  the particular amino acid at that location in the protein. Since p may be up
  to 1000 aa long, the potential number of distinct mRNA sequences is ~N^1000.
  So, we calculate the number modulo 1000000 to avoid integer overflow.
  """
  num_mrna = 1
  for aa in p:
    num_mrna = (num_mrna * num_aa_codons[aa]) % 1000000
  # Now account for stop codons
  num_mrna = (num_mrna * num_aa_codons["Stop"]) % 1000000
  return num_mrna

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  for filename in sys.argv[1:]:
    try:
      with open(filename) as f:
        p = f.read().strip()
    except IOError:
      p = filename
    print(mrna(p))
