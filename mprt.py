#!/usr/bin/env python

"""
Finding a protein motif.
  Given: at most 15 UniProt Protein Database access IDs.
  Return: for each protein possessing the N-glycosylation motif, output its
          given access ID followed by a list of locations in the protein string
          where the motif can be found.

Sample dataset:
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
Sample output:
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614

Usage: mprt <FILE1 | protein1> [FILE2 | protein2]
"""

import urllib.request

uniprot = "http://www.uniprot.org/uniprot/"
fasta = ".fasta"

class Motif(object):
  """
  A motif, or a sort of regular expression for protein strings. Motifs may
  encode rules to match certain parts of a string of amino acids. Separate
  characters must be matched literally, characters within {} are excluded,
  and characters within [] are matched "either/or".
  """

  def __init__(self, motif_string):
    """
    Create a Motif with rules based on a motif string.
    """
    self.motif = []
    rule = "is"
    seq = ""
    for c in motif_string:
      if c == '{':
        rule = "not"
        seq = ""
      elif c == '}':
        self.motif.append((rule, seq))
        rule = "is"
        seq = ""
      elif c == '[':
        rule = "or"
        seq = ""
      elif c == ']':
        self.motif.append((rule, seq))
        rule = "is"
        seq = ""
      else:
        if rule != "is":
          seq += c
        else:
          self.motif.append((rule, c))

  def __str__(self):
    """
    Output the string representation of a motif.
    """
    motif = ""
    for rule in self.motif:
      if rule[0] == "not":
        motif += '{' + rule[1] + '}'
      elif rule[0] == "or":
        motif += '[' + rule[1] + ']'
      else:
        motif += rule[1]
    return motif

  def __len__(self):
    """
    Output the length of the motif if it were to match a string.
    """
    return len(self.motif)

  def __eq__(self, other):
    """
    Can be used to compare this motif with a string. Returns true if motif
    is a protein that matches the other string based on motif rules.
    """
    if self.__len__() != len(other):
      return False
    for i in range(len(other)):
      if self.motif[i][0] == "is" and other[i] != self.motif[i][1]:
        return False
      elif self.motif[i][0] == "or" and other[i] not in self.motif[i][1]:
        return False
      elif self.motif[i][0] == "not" and other[i] in self.motif[i][1]:
        return False

    return True

n_glycosylation = Motif("N{P}[ST]{P}")

def mprt(proteins, motif):
  """
  From a list of proteins, accesses each one by ID at the UniProt database,
  retrieves the FASTA format data file, and finds all locations at which
  motif appears. The retured dict contains ID => list of locations for each
  protein in which motif appears.
  NB: the positions are zero-indexed, while Rosalind expects 1-indexed answers.
  """
  results = {}
  for protein in proteins:
    print("Fetching data for", protein, "...")
    try:
      with urllib.request.urlopen(uniprot + protein + fasta) as response:
        info = response.readline().strip()
        protein_string = ""
        for line in response:
          protein_string += str(line.strip(), encoding = "UTF-8")
    except urllib.error.URLError:
      print("Skipping protein", protein, ": unable to fetch data.")
      continue

    # Traverse protein string, looking for motif
    motif_length = len(motif)
    positions = []
    for i in range(len(protein_string) - motif_length + 1):
      if motif == protein_string[i:i+motif_length]:
        positions.append(i)

    results[protein] = positions

  return results

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  for filename in sys.argv[1:]:
    try:
      with open(sys.argv[1]) as f:
        proteins = f.read().split()
    except IOError:
      proteins = [ filename ]

    locations = mprt(proteins, n_glycosylation)
    print("... done.")
    print("--------------------------")
    for protein in proteins:
      locs = locations.get(protein, [])
      if len(locs) != 0:
        print(protein, ' '.join(str(i+1) for i in locs), sep = '\n')
