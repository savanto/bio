#!/usr/bin/env python

"""
Enumerating k-mers lexicographically.
  Given: a collection of at most 10 symbols defining an ordered alphabet, and
         a positive integer n (n <= 10).
  Return: all strings of length n that can be formed from the alphabet, ordered
          lexicographically.

Sample dataset:
T A G C
2
Sample output:
TT
TA
TG
TC
AT
AA
AG
AC
GT
GA
GG
GC
CT
CA
CG
CC

Usage: lexf <FILE | [a1 [a2 [a3 [...]]]] [n]>
       FILE must have a line of space-separated symbols and a line with n.
       Alternatively, symbols can be specified on the command line, terminated
          by n.
"""

def lexf(symbols, n, word = "", words = []):
  """
  Recursively forms words of length n from given symbols. This is equivalent to
  (symbols choose n) with replacement. Words are returned in a list in 
  lexicographical order defined by the order of the symbols.
  """
  if len(word) == n:
    words.append(word)
  else:
    for s in symbols:
      lexf(symbols, n, word + s, words)
  return words

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  elif len(sys.argv) == 2:
    try:
      with open(sys.argv[1]) as f:
        symbols = f.readline().strip().split()
        n = int(f.readline().strip())
    except ValueError:
      print("Invalid input for n in file", sys.argv[1])
      sys.exit(1)
    except IOError:
      print("Unable to open/read file", sys.argv[1])
      sys.exit(1)

  else:
    try:
      n = int(sys.argv[-1])
    except ValueError:
      print("Invalid input for n --", sys.argv[-1])
      sys.exit(1)
    symbols = sys.argv[1:-1]

  for word in lexf(symbols, n):
    print(word)
