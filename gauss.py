''' This program implements the Gauss lattice reduction algorithm. It takes as input 
base vectors of an 2 dimensional lattice and outputs an basis that is more orthogonal.
The user inputs the name of the file containing the basis on the command line. For example
"python gauss.py input.txt". The input file must contain a square matrix with base vectors of the lattice as rows.
Coordinates must be separated by a space.
The first vector of the output basis is the shortest non-zero vector of the lattice. '''

import numpy as np
import sys

def input_handler(filename):
	try:
		with open(filename, 'r') as infile:
			matrix = np.empty([2, 2])
			i = 0
			infile.seek(0)
			for line in infile:
				matrix[i] = [float(x) for x in line.split()]
				i = i + 1
	except Exception as e:
		print(e)
		sys.exit(0)
	return matrix

def gauss(basis):	
	m = 1
	while m != 0:
		if np.linalg.norm(basis[0]) > np.linalg.norm(basis[1]):
			basis[[1, 0]] = basis[[0, 1]]	
		m = np.rint((np.dot(basis[0],basis[1])) / np.linalg.norm(basis[0]) ** 2)
		if m == 0:
			print(basis)
		else:
			basis[1] = basis[1] - m * basis[0]
			
filename = sys.argv[-1]
base = input_handler(filename)
gauss(base)