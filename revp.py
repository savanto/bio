#!/usr/bin/env python

"""
Locating restriction sites.
  Given: a DNA string of length at most 1 kbp in FASTA format.
  Return: the position and length of every reverse palindrome in the string
          having length between 4 and 12. You may return these pairs in any
          order.

Sample dataset:
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
Sample output:
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4

Usage: revp <FILE | s>
"""

from revc import revc

def revp(s):
  """
  Finds all reverse palindromes in s with length between 4 and 12, and returns
  a list of tuples defining the palindrome's starting position and length.
  NB: starting positions of palindromes are 0-indexed, while Rosalind expects
  1-indexed positions.
  """
  palindromes = []
  for k in range(12, 3, -1):
    for i in range(len(s) - k + 1):
      substr = s[i:i+k]
      if substr == revc(substr):
        palindromes.append((i, k))
  return palindromes


if __name__ == "__main__":  
  import sys
  from fasta import fasta_string
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  try:
    with open(sys.argv[1]) as f:
      s = fasta_string(sys.argv[1])
  except IOError:
    s = sys.argv[1]

  for palindrome in revp(s):
    print(palindrome[0] + 1, palindrome[1])
