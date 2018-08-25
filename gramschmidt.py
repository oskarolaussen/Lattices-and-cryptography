''' This program takes as input the base vectors of a vector space and outputs an orthogonal basis for that space using the Gram-Schmidt process.
The user inputs the name of the file containing the basis on the command line. For example
"python gramschmidt.py input.txt". The input file must contain the base vectors of as lines.
Coordinates must be separated by a space. '''

import sys
import numpy as np

def input_handler(filename):
	try:
		with open(filename, 'r') as infile:
			number_of_vectors = sum((1 for line in infile)) #counts lines in infile.
			infile.seek(0)
			dimension = len(infile.readline().split())
			basis = np.empty([number_of_vectors, dimension])
			i = 0
			infile.seek(0)
			for line in infile:
				basis[i] = [float(x) for x in line.split()]
				i = i + 1
	except Exception as e:
		print(e)
		sys.exit(0)
	return basis, number_of_vectors, dimension

def gramschmidt(basis, number_of_vectors, dimension): 
	orthogonal_basis = np.empty([number_of_vectors, dimension])
	orthogonal_basis[0] = basis[0]
	u = np.zeros([number_of_vectors, dimension])
	for n in range(1, number_of_vectors):
		sum = np.zeros(dimension)
		for j in range(n):
			u[n][j] = basis[n].dot(orthogonal_basis[j]) / orthogonal_basis[j].dot(orthogonal_basis[j])
		for k in range(n):
			sum = u[n][k] * orthogonal_basis[k] + sum
		orthogonal_basis[n] = np.subtract(basis[n],sum)
	print(orthogonal_basis)
	
filename = sys.argv[-1]
base, number_of_vectors, dimension = input_handler(filename)
gramschmidt(base, number_of_vectors, dimension)