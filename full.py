#!/usr/bin/env python

"""
Inferring peptide from full spectrum.
  Given: a list L containing 2n + 3 positive real numbers (n <= 100). The first
         number in L is the parent mass of a peptide P, and all other numbers
         represent the masses of some b-ions and y-ions of P (in no particular
         order). You may assume that if the mass of a b-ion is present, then so
         is that of its complementary y-ion, and vice-versa.
  Return: a protein string t of length n for which there exist two positive
          real numbers w1 and w2 such that for every prefix p and suffix s of t,
          each of w(p) + w1 and w(s) + w2 is equal to an element of L. (In
          other words, there exists a protein string whose t-prefix and t-suffix
          weights correspond to the non-parent mass values of L). If multiple
          solutions exist, you may output any one.

Sample dataset:
1988.21104821
610.391039105
738.485999105
766.492149105
863.544909105
867.528589105
992.587499105
995.623549105
1120.6824591
1124.6661391
1221.7188991
1249.7250491
1377.8200091
Sample output:
KEKEP

Usage: full <FILE>
"""

from prtm import monoisotopic_masses

epsilon = 0.001

def full(L):
  """
  Infers protein from given parent mass and full spectrum by comparing prefix
  masses to each other and building up the sequence.
  """
  protein_length = (len(L) - 3) / 2
  protein = ""
  last_prefix = 1
  for i in range(2, len(L)):
    mass = L[i] - L[last_prefix]
    for aa, aa_mass in monoisotopic_masses.items():
      found = False
      if abs(mass - aa_mass) <= epsilon:
        protein += aa
        found = True
        last_prefix = i
        break
      if len(protein) == protein_length:
        return protein

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  try:
    with open(sys.argv[1]) as f:
      L = list(float(i) for i in f.readlines())
  except ValueError:
    print("Invalid values for L in file", sys.argv[1])
    sys.exit(1)
  except IOError:
    print("Unable to open/read file", sys.argv[1])
    sys.exit(1)

  print(full(L))
