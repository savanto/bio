#!/usr/bin/env python

"""
Finding a shared motif.
  Given: a collection of k (k <= 100) DNA strings of length at most 1 kbp
         each in FASTA format.
  Return: a longest common substring of the collection. (If multiple
          solutions exists, you may return any single solution.)

Sample dataset:
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
Sample output:
AC

Usage: lcsm <FASTA FILE>
"""

def lcsm(dna_strings):
  """
  """
  # First pass: find occurances of A, C, G, T in dna strings
  ldna = len(dna_strings)
  motifs = { 'A': [[] for i in range(ldna)], 'C': [[] for i in range(ldna)],
      'G': [[] for i in range(ldna)], 'T': [[] for i in range(ldna)] }
  for i in range(ldna):
    for j in range(len(dna_strings[i])):
      motifs[dna_strings[i][j]][i].append(j)

  # Prune first set of motifs
  pruned = []
  for motif in motifs:
    for locs in motifs[motif]:
      if len(locs) == 0:
        pruned.append(motif)
        break
  for p in pruned:
    del(motifs[p])

  # Subsequent passes: extend motifs that remain, check for them in all strings,
  # and prune those that do not pass.
  length = 2
  lcm = []
  while len(motifs) != 0:
    lcm = []
    for m in motifs:
      lcm.append(m)

    lmotifs = {}
    for m in motifs:
      for i in range(ldna):
        for j in motifs[m][i]:
          motif = dna_strings[i][j:j+length]
          if len(motif) == length:
            if motif not in lmotifs:
              lmotifs[motif] = [[] for k in range(ldna)]
            lmotifs[motif][i].append(j)

    # Prune
    pruned = []
    for m in lmotifs:
      for locs in lmotifs[m]:
        if len(locs) == 0:
          pruned.append(m)
          break
    for p in pruned:
      del(lmotifs[p])

    motifs = lmotifs
    length += 1

  return lcm

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  from fasta import fasta_list
  try:
    dna_strings = fasta_list(sys.argv[1])
  except IOError:
    print("Could not open/read FASTA file", sys.argv[1])
    sys.exit(1)

  for motif in lcsm(dna_strings):
    print(motif)
