#!/usr/bin/env python

"""
Ordering strings of varying length lexicographically.
  Given: a permutation of at most 12 symbols defining an ordered alphabet A
         and a positive integer n (n <= 4).
  Return: all strings of length at most n formed from A, ordered
          lexicographically. (Note: as in "Enumerating k-mers lexicographically",
          alphabet order is based on the order in which the symbols are given).

Sample dataset:
D N A
3
Sample output:
D
DD
DDD
DDN
DDA
DN
DND
DNN
DNA
DA
DAD
DAN
DAA
N
ND
NDD
NDN
NDA
NN
NND
NNN
NNA
NA
NAD
NAN
NAA
A
AD
ADD
ADN
ADA
AN
AND
ANN
ANA
AA
AAD
AAN
AAA

Usage: lexv <FILE | [a1 [a2 [a3 [...]]]] [n]>
       FILE must have a line of space-separated symbols and a line with n.
       Alternatively, symbols can be specified on the command line, terminated
          by n.
"""

def lexv(symbols, n, word = "", words = []):
  """
  Recursively generates all possible sets from the given set of symbols with
  1 < word_length < n, and returns a list of words that are formed by these
  sets. Words are in lexicographical order defined by the order of the given
  symbols.
  """
  if len(word) != 0:
    words.append(word)
  if len(word) < n:
    for s in symbols:
      lexv(symbols, n, word + s, words)
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

  for word in lexv(symbols, n):
    print(word)
