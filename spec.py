#!/usr/bin/env python

"""
Inferring protein from spectrum.
  Given: a list L of n (n <= 100) positive real numbers.
  Return: a protein string of length n - 1 whose prefix spectrum is equal to L
          (if multiple solutions exist, you may output any one of them).
          Consult the monoisotopic mass table.

Sample dataset:
3524.8542
3710.9335
3841.974
3970.0326
4057.0646
Sample output:
WMQS

Usage: spec <FILE1> [FILE2] [FILE3] ...
"""

from prtm import monoisotopic_masses

epsilon = 0.001

def spec(L):
  """
  Calculates differences between every adjacent entry in L to infer amino acid
  from the monoisotopic masses table. Amino acids are matched to within 0.001Da
  """
  # TODO output all possible proteins (since weights are not unique)
  protein = []
  for n in range(1, len(L)):
    mass = L[n] - L[n-1]
    for aa, aa_mass in monoisotopic_masses.items():
      if abs(mass - aa_mass) <= epsilon:
        protein.append(aa)
        break
  return ''.join(protein)


if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  for filename in sys.argv[1:]:
    try:
      with open(filename) as f:
        L = list(float(i) for i in f.read().strip().split())
    except ValueError:
      print("Skipping file", filename, ": invalid input in file.")
      continue
    except IOError:
      print("Skipping file", filename, ": could not open/read file.")
      continue

    print(spec(L))
