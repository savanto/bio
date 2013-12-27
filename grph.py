#!/usr/bin/env python

"""
Overlap graphs.
  Given: a collection of DNA strings in FASTA format having total length at
         most 10 kbp.
  Return: The adjacency list corresponding to O3. You may return edges in any
          order.

Sample dataset:
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
Sample output:
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323

Usage: grph <FILE> [k]
       If k is omitted, a default value of 3 is used.
"""

def grph(dna_strings, k):
  """
  Traverses dict dna_strings produces a list of tuples representing the
  vertices of an overlap graph (two DNA strings overlap if the suffix of length
  k of one matches the prefix of length k of another. A string may not overlap
  with itself).
  """
  graph = []
  for suffix_id, suffix_dna in dna_strings.items():
    for prefix_id, prefix_dna in dna_strings.items():
      if suffix_dna[-k:] == prefix_dna[:k] and suffix_id != prefix_id:
        graph.append((suffix_id, prefix_id))
  return graph

if __name__ == "__main__":  
  import sys
  from fasta import fasta_dict
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  dna_strings = fasta_dict(sys.argv[1])
  if len(sys.argv) > 2:
    try:
      k = int(sys.argv[2])
    except ValueError:
      print("Invalid k value supplied, using 3 [default].")
      k = 3
  else:
    k = 3
  graph = grph(dna_strings, k)
  for vertex in graph:
    print(' '.join(vertex))
