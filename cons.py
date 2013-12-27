#!/usr/bin/env python

"""
Consensus and profile.
  Given: a collection of at most 10 DNA strings of equal length (at most 1kbp)
         in FASTA format.
  Return: a consensus string and profile matrix for the collection. (If several
          consensus strings exist, then you may return any one of them.)

Sample dataset:
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
Sample output:
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6

Usage: cons <FILE>
"""
def prof(dna_strings):
  """
  Determines and returns profile matrix for dna_strings. Matrix has the form
  {
    'A': [n1, n2, n3, ..., nN],
    'C': [n1, n2, n3, ..., nN],
    'G': [n1, n2, n3, ..., nN],
    'T': [n1, n2, n3, ..., nN]
  }
  """
  length = len(dna_strings[0])
  profile = {}
  profile['A'] = [0] * length
  profile['C'] = [0] * length
  profile['G'] = [0] * length
  profile['T'] = [0] * length
  for pos in range(length):
    for dna_string in dna_strings:
      profile[dna_string[pos]][pos] += 1
  return profile

def cons(profile_matrix):
  """
  Determines and returns consensus string from profile_matrix.
  """
  length = len(profile_matrix['A'])
  consensus = ""
  for pos in range(length):
    max_count = 0
    max_base = 'A'
    for base, counts in profile.items():
      if counts[pos] > max_count:
        max_count = counts[pos]
        max_base = base
    consensus += max_base
  return consensus

if __name__ == "__main__":  
  import sys
  from fasta import fasta_list
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  try:
    dna_strings = fasta_list(sys.argv[1])
  except IOError:
    print("Unable to open/read FASTA file", sys.argv[1])
    sys.exit(1)

  profile = prof(dna_strings)
  consensus = cons(profile)

  print(consensus)
  print("A:", ' '.join(str(i) for i in profile['A']))
  print("C:", ' '.join(str(i) for i in profile['C']))
  print("G:", ' '.join(str(i) for i in profile['G']))
  print("T:", ' '.join(str(i) for i in profile['T']))
