#!/usr/bin/env python

"""
Module for parsing FASTA format files.

Usage: fasta <FILE>
"""

def open_file(filename):
  """
  Opens a FASTA format file for parsing.
  """
  try:
    with open(filename) as f:
      lines = f.readlines()
      if lines[0][0] != '>':
        raise IOError
  except IOError:
    raise IOError

  return lines

def append_dict(ID, DNA, data):
  data[ID] = DNA

def append_list(ID, DNA, data):
  data.append(DNA)

def append_tuple_list(ID, DNA, data):
  data.append((ID, DNA))

def fasta(filename, data, append_function):
  """
  Produces the desired data structure holding the contents of a FASTA file.
  data is the required data structure, append_function is a method for
  appending read-in data to the structure.
  """
  lines = open_file(filename)
  try:
    line = lines[0].strip()
    if line[0] != '>':
      raise IOError
    else:
      ID = line[1:].strip()
      DNA = ""
    for line in lines[1:]:
      if line[0] == '>':
        append_function(ID, DNA, data)
        DNA = ""
        ID = line[1:].strip()
      else:
        DNA += line.strip()
    append_function(ID, DNA, data)
  except IOError:
    raise IOError

  return data

def fasta_dict(filename):
  """
  Produces a dict containing the data contents of a FASTA file. The dict is
  keyed by the info line of the FASTA file, and the value field is the DNA
  string. NB: data are not guaranteed to be in the order read from file. For
  that, use fasta_list or fasta_tuple_list.
  """
  try:
    data_dict = fasta(filename, {}, append_dict)
  except IOError:
    raise IOError

  return data_dict

def fasta_list(filename):
  """
  Produces a list containing the data contents of a FASTA file. The list
  contains only the DNA strings (the info line is ommitted), but the strings
  are in the order read in from the file. If the info line is required, use
  fasta_dict or fasta_tuple_list.
  """
  try:
    data_list = fasta(filename, [], append_list)
  except IOError:
    raise IOError

  return data_list

def fasta_tuple_list(filename):
  """
  Produces a list of tuples containing the data contents of a FASTA file. The
  list contains tuples of the form (ID, DNA), and the strings are in the order
  read in from the file. If order is not important, use fasta_dict, or if info
  is not important, use fasta_list.
  """
  try:
    data_tuple_list = fasta(filename, [], append_tuple_list)
  except IOError:
    raise IOError

  return data_tuple_list

def fasta_string(filename):
  """
  Produces the DNA string of the first DNA data in the FASTA file.
  Helper function for compatibility.
  """
  return fasta_list(filename)[0]

if __name__ == "__main__":  
  import sys
  if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

  try:
    data_dict = fasta_dict(sys.argv[1])
    data_list = fasta_list(sys.argv[1])
    data_tuple_list = fasta_tuple_list(sys.argv[1])
  except IOError:
    print("Unable to open/read FASTA file", sys.argv[1])
    sys.exit(1)

  if len(data_dict) == 0 or len(data_list) == 0 or len(data_tuple_list) == 0:
    print("No data in FASTA file", sys.argv[1])
  else:
    print("Data in dict:")
    for ID, DNA in data_dict.items():
      print(ID, DNA, sep = '\n')
    print()
    print("Data in list:")
    for DNA in data_list:
      print(DNA)
    print()
    print("Data in tuple list:")
    for tup in data_tuple_list:
      print(tup[0], tup[1], sep = '\n')
