#!/usr/bin/env python

"""
Completing a tree.
  Given: a positive integer n (n <= 1000) and an adjacency list corresponding
         to a graph on n nodes that contain no cycles.
  Return: the minimum number of edges that must be added to the graph to
          produce a tree.

Sample dataset:
10
1 2
2 8
4 10
5 9
6 10
7 9
Sample output:
3

Usage: tree <FILE>
"""

def flood_fill(node, adj_list, connected):
  """
  Flood-fill algorithm performs a depth-first search on all of the nodes
  adjacent to node, and marks them as connected.
  """
  if not connected[node]:
    connected[node] = True
    for next_node in adj_list[node]:
      flood_fill(next_node, adj_list, connected)

def tree(n, adj_list):
  """
  Uses flood-fill algorithm to compute the number of disconnected subgraphs
  defined by nodes 1 .. n and edges adj_list.
  Number of edges required to connect all subgraphs is #subgraphs - 1.
  """
  connected = [ False for i in range(n) ]
  subgraphs = 0
  for node in range(n):
    if not connected[node]:
      subgraphs += 1
      flood_fill(node, adj_list, connected)
  return subgraphs - 1

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  try:
    with open(sys.argv[1]) as f:
      n = int(f.readline().strip())
      proto_adj_list = []
      for line in f.readlines():
        proto_adj_list.append(list(int(i) for i in line.strip().split()))
  except IOError:
    print("Unable to open/read file", sys.argv[1])
    sys.exit(1)
  except ValueError:
    print("Invalid values in file", sys.argv[1])
    sys.exit(1)
  # Convert Rosalind adjacency list to something easier to work with
  adj_list = [ [] for i in range(n) ]
  for edge in proto_adj_list:
    adj_list[edge[0]-1].append(edge[1]-1)
    adj_list[edge[1]-1].append(edge[0]-1)
  print(tree(n, adj_list))
