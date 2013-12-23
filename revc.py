#!/usr/bin/env python

"""
Complementing a strand of DNA.
  Given: a DNA string s of length at most 1000 bp.
  Return: the reverse complement sc of s.

Sample dataset:
AAAACCCGGT
Sample output:
ACCGGGTTTT

Usage: revc <FILE1 | s1> [FILE2 | s2] ...
"""

complements = { 'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A' }

def revc(s):
  """
  Returns the reverse complement of a strand of DNA s.
  """
  rev_comp = []
  for bp in reversed(s):
    rev_comp.append(complements[bp])

  return ''.join(rev_comp)

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
  print(revc(s))
