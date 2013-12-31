#!/usr/bin/env python

"""
Matching a spectrum to a protein.
  Given: a positive integer n followed by a collection of n protein strings
         s1, s2, ..., sn and a multiset R of positive numbers (corresponding to
         the complete spectrum of some unknown protein string).
  Return: the maximum multiplicity of R (-) S[sk] taken over all strings sk,
          followed by the string sk for which this multiplicity occurs (you may
          output any such value if multiple solutions exist).

Sample dataset:
4
GSDMQS
VWICN
IASWMQS
PVSMGAD
445.17838
115.02694
186.07931
314.13789
317.1198
215.09061
Sample output:
3
IASWMQS

Usage: prsm <FILE>
"""

from prtm import monoisotopic_masses
from conv import conv

def prsm(proteins, R):
  """
  Calculates the complete spectrum for each protein string by doing look ups
  in the monoisotopic_masses table and calculating masses of all prefixes and
  suffixes of protein. Then does a convolution on each spectrum with the given
  spectrum of the unknown protein R. The maximum multiplicity over all protein
  strings and the string with this multiplicity are returned.
  """
  max_multiplicity = 0
  sk = ""
  for protein in proteins:
    S = []
    mass = 0
    # Prefix masses
    for aa in protein[:-1]:
      mass += monoisotopic_masses[aa]
      S.append(mass)
    mass += monoisotopic_masses[protein[-1]]
    # Suffix masses
    num_prefixes = len(S)
    for i in range(num_prefixes):
      S.append(mass - S[i])

    # Calculate convolution
    multiplicity, _ = conv(R, S)
    if multiplicity >= max_multiplicity:
      max_multiplicity = multiplicity
      sk = protein

  return max_multiplicity, sk


if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  try:
    with open(sys.argv[1]) as f:
      n = int(f.readline().strip())
      proteins = []
      for i in range(n):
        proteins.append(f.readline().strip())
      R = list(float(i) for i in f.readlines())
  except ValueError:
    print("Invalid values in file", sys.argv[1])
    sys.exit(1)
  except IOError:
    print("Unable to open/read file", sys.argv[1])
    sys.exit(1)

  for v in prsm(proteins, R):
    print(v)
