#!/usr/bin/env python

"""
Introduction to alternative splicing.
  Given: positive integers n and m with 0 <= m <= n <= 2000.
  Return: the sum of combinations C(n, k) for all k satisfying m <= k <=n,
          modulo 1000000. In shorthand, sum[k=m..n]C(n, k).

Sample dataset:
6 3
Sample output:
42

Usage: aspc <FILE | n m>
"""

def aspc(n, m):
  """
  Calculates and returns the sum of all combinations C(n, k) for k from m to n.
  C(n, k) = n! / (k!(n-k)!) = n(n-1)(n-2)...(n-k+1) / k!
  """
  # Calculate initial k! for k = m
  k_factorial = 1
  for i in range(m, 1, -1):
    k_factorial = (k_factorial * i)
  # Calculate initial numerator for k = m
  numerator = 1
  for i in range(n, n-m, -1):
    numerator = (numerator * i)
  # Sum up combos
  combos = numerator // k_factorial
  for k in range(m + 1, n + 1):
    k_factorial = (k_factorial * k)
    numerator = (numerator * (n - k + 1))
    combos += numerator // k_factorial

  return combos % 1000000


if __name__ == "__main__":  
  import sys
  if len(sys.argv) == 2:
    try:
      with open(sys.argv[1]) as f:
        n, m = (int(i) for i in f.readline().strip().split())
    except ValueError:
      print("Invalid values for n and m in file", sys.argv[1])
      sys.exit(1)
    except IOError:
      print("Unable to open/read file", sys.argv[1])
      sys.exit(1)

  elif len(sys.argv) == 3:
    try:
      n, m = (int(i) for i in sys.argv[1:3])
    except ValueError:
      print("Invalid values for n and m --", sys.argv[1])
      sys.exit(1)

  else:
    print(__doc__)
    sys.exit(1)

  print(aspc(n, m))
