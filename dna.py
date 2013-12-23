#!/usr/bin/env python

"""
Counting DNA nucleotides.
  Given: a DNA string s of length at most 1000 nt.
  Return: four integers (separated by spaces) counting the respective number
          of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample dataset:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
Sample output:
20 12 17 21

Usage: dna <FILE1 | s1> [FILE2 | s2] ...
"""

def dna(s):
  """
  Counts the frequency of each nucleotide in the DNA string s.
  """
  counts = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 }
  for nt in s:
    try:
      counts[nt] += 1
    except KeyError:
      pass
  return counts

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
    counts = dna(s)
    print(counts['A'], counts['C'], counts['G'], counts['T'])
