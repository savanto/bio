#!/usr/bin/env python

"""
Mortal Fibonacci rabbits.
  Given: positive integers n <= 100 and m <= 20
  Return: the total number of pairs of rabbits that will remain after the
          n-th month if all rabbits live for m months.

Sample dataset:
6 3
Sample output:
4

Usage: fibd <FILE1 | n m>
"""

def fibd(n, m):
  """
  Calculates final element in Fibonacci-like sequence of rabbit pairs that
  begin at 1 pair, mature after 1 month, produce a litter of 1 pair, and
  die after m months.
  """
  # Start with 1 pair of immature rabbits, and no adults
  rabbits = [ (1, 0) ]
  for i in range(1, n):
    # Offspring by adults
    babies = rabbits[-1][1]
    # Rabbits that mature from babies to adults
    adults = sum(rabbits[-1])
    # Rabbits that die
    if m <= i:
      adults -= rabbits[i-m][0]
    # Record new generation
    rabbits.append((babies, adults))

  return sum(rabbits[-1])

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  elif len(sys.argv) < 3:
    try:
      with open(sys.argv[1]) as f:
        n, m = (int(i) for i in f.read().strip().split())
    except IOError:
      print("Unable to read file", sys.argv[1])
      sys.exit(1)
    except ValueError:
      print("Unable to read n, m from file", sys.argv[1])
      sys.exit(1)
  else:
    try:
      n, m = (int(i) for i in sys.argv[1:])
    except ValueError:
      print("Invalid n, m arguments --", ' '.join(sys.argv[1:]))
      sys.exit(1)
  print(fibd(n, m))
