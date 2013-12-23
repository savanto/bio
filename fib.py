#!/usr/bin/env python

"""
Rabbits and recurrence relations.
  Given: positive integers n <= 40 and k <= 5
  Return: The total number of rabbit pairs that will be present after n
          months if we begin with 1 pair and in each generation, every
          pair of reproduction-age rabbits produces a litter of k rabbit
          pairs (instead of only 1 pair).

Sample dataset:
5 3
Sample output:
19

Usage: fib <FILE1 | n k>
"""

def fib(n, k):
  """
  Calculates the final term in a Fibonacci-like sequence of rabbit pairs
  after n months and with each rabbit pair having a litter of size k.
  """
  baby = 1
  adult = 0
  for i in range(n-1):
    litter = adult * k
    adult += baby
    baby = litter
  return adult + baby

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  elif len(sys.argv) < 3:
    try:
      with open(sys.argv[1]) as f:
        n, k = (int(i) for i in f.read().strip().split())
    except IOError:
      print("Cannot read file", sys.argv[1])
      sys.exit(1)
    except ValueError:
      print("Cannot read n, k from file", sys.argv[1])
      sys.exit(1)
  else:
    try:
      n, k = (int(i) for i in sys.argv[1:])
    except ValueError:
      print("Invalid n, k arguments --", ' '.join(sys.argv[1:]))
      sys.exit(1)
  print(fib(n, k))
