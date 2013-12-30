#!/usr/bin/env python

"""
Introduction to pattern matching.
  Given: a list of at most 100 DNA strings of length at most 100 bp, none of
         which is a prefix of another.
  Return: the adjacency list corresponding to the trie T for these patterns, in
          the following format. If T has n nodes, first label the root with 1
          and then label the remaining nodes with the integers 2 through n in
          any order you like. Each edge of the adjacency list of T will be
          encoded by a triple containing the integer representing the edge's
          parent node, followed by the integer representing the edge's child
          node, and finally the symbol labeling the edge.

Sample dataset:
ATAGA
ATC
GAT
Sample output:
1 2 A
2 3 T
3 4 A
4 5 G
5 6 A
3 7 C
1 8 G
8 9 A
9 10 T

Usage: trie <FILE1 | s1> [FILE2 | s2] [FILE3 | s3] ...
"""

class Node(object):
  """
  A Node of the trie. Stores its node id, the symbol that the edge from this
  node to its parent encodes, and a list of children nodes.
  NB: the root Node will have no parent, and no edge to a parent, and no symbol.
  """
  # Static node id count
  i = 0

  def __init__(self, sym = ''):
    """
    Initializes a Node with given symbol. With no arguments, creates a 'root'
    node with no symbol. Node will have empty children list.
    """
    Node.i += 1
    self.i = Node.i
    self.sym = sym
    self.children = []

  def insert(self, s):
    """
    Recursively insert string s into trie character by character.
    """
    if len(s) != 0:
      in_trie = False
      for child in self.children:
        if child.sym == s[0]:
          in_trie = True
          child.insert(s[1:])
          break
      if not in_trie:
        self.children.append(Node(s[0]))
        self.children[-1].insert(s[1:])

  def get_adj_list(self):
    """
    Traverses trie and returns an adjacency list of edges, with each edge
    having the form (parent, child, symbol).
    """
    edges = []
    for child in self.children:
      edges.append((self.i, child.i, child.sym))
      edges += child.get_adj_list()
    return edges

def trie(dna_strings):
  """
  Constructs trie from dna_strings and returns adjacency list defining the
  edges of the trie. Each entry in the list corresponds to an edge in the form
  of a triple (parent, child, symbol) eg. (1, 2, 'A').
  """
  trie = Node()
  for s in dna_strings:
    trie.insert(s)

  return trie.get_adj_list()

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  dna_strings = []
  for filename in sys.argv[1:]:
    try:
      with open(filename) as f:
        dna_strings += f.read().strip().split()
    except IOError:
      dna_strings.append(filename)

  for edge in trie(dna_strings):
    print(' '.join(str(i) for i in edge))
