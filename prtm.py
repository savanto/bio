#!/usr/bin/env python

"""
Calculating protein mass.
  Given: a protein string P of length at most 1000 aa.
  Return: the total weight of P. Consult the monoisotopic mass table.

Sample dataset:
SKADYEK
Sample output:
821.392

Usage: prtm <FILE1 | P1> [FILE2 | P2] ...
"""

monoisotopic_masses = { 'A':  71.03711, 'C': 103.00919, 'D': 115.02694,
                        'E': 129.04259, 'F': 147.06841, 'G':  57.02146,
                        'H': 137.05891, 'I': 113.08406, 'K': 128.09496,
                        'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
                        'P':  97.05276, 'Q': 128.05858, 'R': 156.10111,
                        'S':  87.03203, 'T': 101.04768, 'V':  99.06841,
                        'W': 186.07931, 'Y': 163.06333 }

def prtm(P):
  """
  Sums the monoisotopic masses of the amino acids in the given protein P.
  """
  weight = 0
  for aa in P:
    weight += monoisotopic_masses.get(aa, 0)
  return weight

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  for filename in sys.argv[1:]:
    try:
      with open(filename) as f:
        P = f.read().strip()
    except IOError:
      P = filename
    print("{0:.3f}".format(prtm(P)))
