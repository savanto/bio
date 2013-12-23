#!/usr/bin/env python

"""
Transcribing DNA into RNA.
  Given: a DNA string t having length at most 1000 nt.
  Return: the transcribed RNA string of t (all thymine T bases are converted
          into uracil U).

Sample dataset:
GATGGAACTTGACTACGTAAATT
Sample output:
GAUGGAACUUGACUACGUAAAUU

Usage: rna <FILE1 | t1> [FILE2 | t2] ...
"""

def rna(t):
  """
  Transcribes DNA string t into RNA equivalent.
  """
  trans = []
  for nt in t:
    if nt == 'T':
      trans.append('U')
    else:
      trans.append(nt)

  return ''.join(trans)

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  for filename in sys.argv[1:]:
    try:
      with open(filename) as f:
        t = f.read().strip()
    except IOError:
      t = filename
    print(rna(t))
