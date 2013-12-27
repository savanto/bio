#!/usr/bin/env python

"""
Open reading frames.
  Given: a DNA string s of length at most 1 kbp in FASTA format.
  Return: every distinct candidate protein string that can be translated from
          open reading frames of s (including reverse complement!)

Sample dataset:
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGA
TCCGAGTAGCATCTCAG
Sample output:
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE

Usage: orf <FILE | s>
"""

from revc import revc

dna_codons = { "TTT": 'F',   "CTT": 'L',   "ATT": 'I',   "GTT": 'V',
               "TTC": 'F',   "CTC": 'L',   "ATC": 'I',   "GTC": 'V',
               "TTA": 'L',   "CTA": 'L',   "ATA": 'I',   "GTA": 'V',
               "TTG": 'L',   "CTG": 'L',   "ATG": 'M',   "GTG": 'V',
               "TCT": 'S',   "CCT": 'P',   "ACT": 'T',   "GCT": 'A',
               "TCC": 'S',   "CCC": 'P',   "ACC": 'T',   "GCC": 'A',
               "TCA": 'S',   "CCA": 'P',   "ACA": 'T',   "GCA": 'A',
               "TCG": 'S',   "CCG": 'P',   "ACG": 'T',   "GCG": 'A',
               "TAT": 'Y',   "CAT": 'H',   "AAT": 'N',   "GAT": 'D',
               "TAC": 'Y',   "CAC": 'H',   "AAC": 'N',   "GAC": 'D',
               "TAA": "Stop","CAA": 'Q',   "AAA": 'K',   "GAA": 'E',
               "TAG": "Stop","CAG": 'Q',   "AAG": 'K',   "GAG": 'E',
               "TGT": 'C',   "CGT": 'R',   "AGT": 'S',   "GGT": 'G',
               "TGC": 'C',   "CGC": 'R',   "AGC": 'S',   "GGC": 'G',
               "TGA": "Stop","CGA": 'R',   "AGA": 'R',   "GGA": 'G',
               "TGG": 'W',   "CGG": 'R',   "AGG": 'R',   "GGG": 'G' }

start_codon = "ATG"

def orf(s):
  """
  Traverses DNA string s and its reverse complement, performing lookups for
  DNA codons. All strings beginning with a start codon and terminated by a
  stop codon are translated, and unique protein strings are returned.
  """
  strands = (s, revc(s))
  proteins = set()
  for strand in strands:
    for i in range(len(strand)):
      codon = strand[i:i+3]
      if codon == start_codon:
        protein = ""
        j = i
        try:
          while dna_codons[codon] != "Stop":
            protein += dna_codons[codon]
            j += 3
            codon = strand[j:j+3]
        except KeyError:
          # Not a valid codon => not a valid protein.
          continue
        proteins.add(protein)

  return proteins

if __name__ == "__main__":  
  import sys
  from fasta import fasta_string
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  try:
    s = fasta_string(sys.argv[1])
  except IOError:
    s = sys.argv[1]
  proteins = orf(s)
  for protein in proteins:
    print(protein)
