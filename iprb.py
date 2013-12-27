#!/usr/bin/env python

"""
Mendel's First Law
  Given: three positive integers k, m, and n, representing a population
         containing k + m + n organisms: k individuals are homozygous dominant
         for a factor, m are heterozygous, and n are homozygous recessive.
  Return: the probability that two randomly selected mating organisms will
          produce an individual possessing a dominant allele (and thus
          displaying the dominant phenotype). Assume that any two organisms
          can mate.

Sample dataset:
2 2 2
Sample output:
0.78333

Usage: iprb <FILE | k m n>
"""

def iprb(k, m, n):
  """
  Calculate probability that two randomly selected organisms will produce an
  offspring possessing a dominant allele, given that there are k homozygous
  dominant, m heterzygous, and n homozygous recessive individuals in the
  population.
  """
  pop = k + m + n
  prob = 0
  # Possible pairings and their offspring with a dominant allele
  kk = 4/4
  km = 4/4
  kn = 4/4
  mk = 4/4
  mm = 3/4
  mn = 2/4
  nk = 4/4
  nm = 2/4
  nn = 0/4
  # Probability calculations
  # k branch
  prob += k/pop * (k-1)/(pop-1) * kk
  prob += k/pop * m/(pop-1) * km
  prob += k/pop * n/(pop-1) * kn
  # m branch
  prob += m/pop * k/(pop-1) * mk
  prob += m/pop * (m-1)/(pop-1) * mm
  prob += m/pop * n/(pop-1) * mn
  # n branch
  prob += n/pop * k/(pop-1) * nk
  prob += n/pop * m/(pop-1) * nm
  prob += n/pop * (n-1)/(pop-1) * nn

  return prob

if __name__ == "__main__":  
  import sys
  if len(sys.argv) == 2:
    try:
      with open(sys.argv[1]) as f:
        k, m, n = list(int(i) for i in f.readline().strip().split())
    except IOError:
      print("Unable to open/read file", sys.argv[1])
      sys.exit(1)
    except ValueError:
      print("No valid inputs k, m, n in file", sys.argv[1])
      sys.exit(1)

  elif len(sys.argv) == 4:
    try:
      k, m, n = list(int(i) for i in sys.argv[1:4])
    except ValueError:
      print("No valid inputs for k, m, n --", ' '.join(sys.argv[1:4]))
      print(__doc__)
      sys.exit(1)

  else:
    print(__doc__)
    sys.exit(1)

  print("{0:.5f}".format(iprb(k, m, n)))
