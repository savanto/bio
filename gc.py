#!/usr/bin/env python

"""
Computing GC content.
  Given: at most 10 DNA strings in FASTA format (of length at most 1kbp each)
  Return: the ID of the string having the highest GC-content, followed by the
          GC-content of that string. Permitted error = 0.001.

Sample dataset:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
Sample output:
Rosalind_0808
60.919540

Usage: gc <FASTA_FILE1> [FASTA_FILE2] ...
"""

def gc(dna_strings):
  """
  Traverses dictionary dna_strings which was made by reading a FASTA-formatted
  file and has the form { FASTA_ID: dna_string }, and counts GC percentage
  for each string. The output is a tuple containing the ID and GC-content as a
  percentage of the string with the highest GC content.
  """
  max_gc = ("", 0)
  for ID, dna_string in dna_strings.items():
    gc_content = 0
    for nt in dna_string:
      if nt in "GC":
        gc_content += 1
    gc_content /= len(dna_string)
    if gc_content > max_gc[1]:
      max_gc = (ID, gc_content)

  return max_gc

if __name__ == "__main__":  
  import sys
  from fasta import fasta_dict
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  for filename in sys.argv[1:]:
    try:
      dna_strings = fasta_dict(filename)
    except IOError:
      print("Skipping file", filename, ": unable to open/read file.")
      continue
    max_gc = gc(dna_strings)
    print(max_gc[0], "{0:.6f}".format(max_gc[1] * 100), sep = '\n')
