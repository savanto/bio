#!/usr/bin/env python

"""
Calculating expected offspring
  Given: six positive integers, each of which does not exceed 20,000. The
         integers correspond to the number of couples in a population
         possessing each genotype pairing for a given factor. In order, the six
         given integers represent the number of couples having the following
         genotypes:
            1. AA-AA
            2. AA-Aa
            3. AA-aa
            4. Aa-Aa
            5. Aa-aa
            6. aa-aa
  Return: the expected number of offspring displaying the dominant phenotype in
          the next generation, under the assumption that every couple has
          exactly two offspring.

Sample dataset:
1 0 0 1 0 1
Sample output:
3.5

Usage: iev <file | c1 c2 c3 c4 c5 c6> [k]
       k may be ommitted, in which case it defaults to 2.
"""

def iev(couples, k):
  """
  Calculates the expected number of offspring displaying the dominant phenotype
  in the next generation given the number of each possible pairing couples and
  the number of offspring to each couple k.
  """
  # The probabilities of an offspring with dominant phenotype for each couple
  probs = [1, 1, 1, 0.75, 0.5, 0]
  offspring = 0
  for i in range(6):
    offspring += probs[i] * couples[i]
  offspring *= k

  return offspring

if __name__ == "__main__":  
  import sys
  
  k = 2
  if len(sys.argv) in (2, 3):
    # Data in file
    try:
      with open(sys.argv[1]) as f:
        couples = list(int(i) for i in f.readline().strip().split())
    except IOError:
      print("Unable to open/read file", sys.argv[1])
      sys.exit(1)
    if len(sys.argv) == 3:
      try:
        k = int(sys.argv[2])
      except ValueError:
        print("Invalid k value provided --", sys.argv[2])
        print("Defaulting to k = 2")

  elif len(sys.argv) in (7, 8):
    # Data on command line
    try:
      couples = list(int(i) for i in sys.argv[1:7])
    except ValueError:
      print("Invalid values provided --", ' '.join(sys.argv[1:7]))
      print(__doc__)
      sys.exit(1)
    if len(sys.argv) == 8:
      try:
        k = int(sys.argv[7])
      except ValueError:
        print("Invalid k value provided --", sys.argv[7])
        print("Defaulting to k = 2")

  else:
    print(__doc__)
    sys.exit(1)

  print(iev(couples, k))
