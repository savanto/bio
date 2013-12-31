#!/usr/bin/env python

"""
Using the spectrum graph to infer peptides.
  Given: a list L (of length at most 100) containing positive real numbers.
  Return: the longest protein string that matches the spectrum graph of L (if
          multiple solutions exist, you may output any one of them). Consult
          the monoisotopic masses table.

Sample dataset:
3524.8542
3623.5245
3710.9335
3841.974
3929.00603
3970.0326
4026.05879
4057.0646
4083.08025
Sample output:
WMSPG

Usage: sgra <FILE>
"""

from prtm import monoisotopic_masses

epsilon = 0.001

def traverse(edges, next_node = 0, protein = "", proteins = []):
  """
  Traverse the edges list and produce all possible protein strings.
  """
  if len(edges[next_node]) == 0:
    proteins.append(protein)
  else:
    for edge in edges[next_node]:
      nn, sym = edge
      traverse(edges, nn, protein + sym, proteins)
  return proteins

def sgra(L):
  """
  Creates list of edges of graph of protein amino acids that can be created from
  the given spectrum L. Edges are then traversed and the longest protein string
  is returned.
  """
  node = 0
  edges = {}
  for i in range(len(L)):
    edges[i] = []
  for u, i in zip(L, list(range(len(L)))):
    for v, j in zip(L, list(range(len(L)))):
      if v > u:
        mass = v - u
        for aa, aa_mass in monoisotopic_masses.items():
          if abs(mass - aa_mass) <= epsilon:
            edges[i].append((j, aa))

  proteins = traverse(edges)
  # Return longest possible protein string
  return max(proteins, key = len)

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

  print(sgra(L))
